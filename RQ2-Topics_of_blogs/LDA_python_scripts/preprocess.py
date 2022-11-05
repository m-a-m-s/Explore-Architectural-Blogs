import fileinput
import os
from nltk.stem import WordNetLemmatizer
import nltk.corpus as corpus
import openpyxl
import re
from tqdm import tqdm

DOCUMENTS_FOLDER = "txtfiles"

wordnet = corpus.wordnet
wordnet._exception_map['n']['vs'] = ['versus']
wordnet._exception_map['n']['has'] = ['have']
lemmatizer = WordNetLemmatizer()

def load_replacement_list(filename): 
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    replacement_list = []   
    for col in ws.iter_cols(min_col = 1):
        target_word = col[0].value        
        if (target_word):
            target_word =  target_word.lower().rstrip('\n')
        else:
            target_word = ""
        # empty string in sheet may be read as '""' so we check for it
        if target_word == '""':
            target_word = ""
            
        name_set = set()
        for cell in col[1:]:
            tech_word = cell.value
            if tech_word:
                name_set.add(tech_word.rstrip('\n'))
        replacement_list.append((target_word, name_set))
    return replacement_list

# determines word type for semantic matching
def det_type(word):
    noun = 0
    verb = 0
    adj = 0
    for syn in wordnet.synsets(word):
        if syn.pos() == 'n':
            noun += 1
        if syn.pos() == 'v':
            verb += 1
        if syn.pos() == 'a':
            adj += 1
    if verb > noun and verb > adj:
        return 'v'
    if adj > noun and adj > verb:
        return 'a'
    return 'n'

# simplify differently written same words to a base form
def simplify_term(word, simp_set):
    for [target, keywords] in simp_set:
        if word in keywords:
            word = target
    return word

# matches compound words
def compound_words_matcher(text_line, compound_word_set):  
    for [target, keywords] in compound_word_set:      
        for keyword in keywords:                  
            text_line = re.sub(r"\b%s(\.)?\b" % keyword, target, text_line, flags=re.IGNORECASE)
    return text_line

# replaces keyword with their ontology class name + UID
def ontology_replace(word, ontology_set, simplify_set, occurences):
    match = False
    replace_result = ""
    for [target, keywords] in ontology_set:
        if word in keywords: # keyword already appears in the document
            match = True
            word = simplify_term(word, simplify_set)
            if word not in occurences: # new keyword, attach UID
                count = occurences[target] = occurences[target] + 1
                occurences[word] = target + str(count) if target else "" 
            replace_result = occurences[word]
            break
        elif word.lower() in keywords: # possibly unnecessary, included as a safeguard.
            match = True
            word = simplify_term(word.lower(), simplify_set)
            if word not in occurences:
                count = occurences[target] = occurences[target] + 1
                occurences[word] = target + str(count) if target else ""                
            replace_result = occurences[word]
            break
    return [replace_result, match]

def main():
    path = os.path.join(DOCUMENTS_FOLDER, "category_1_folder")
    sheet_path = os.path.join("preprocessing", "ontology_sheet.xlsx")
    simp_sheet_path = os.path.join("preprocessing", "simplify_ontology.xlsx")    
    ontology_set = load_replacement_list(sheet_path)
    # github won't allow empty directories
    if not os.path.exists("debug_results"):
        os.mkdir("debug_results")
    replaced_path = os.path.join("debug_results", "replaced.txt")
    replaced_words_file = open(replaced_path, 'w+')
    simplify_set = load_replacement_list(simp_sheet_path)
    compound_words_path = os.path.join("preprocessing", "compound_words.xlsx")
    compounds_set = load_replacement_list(compound_words_path)
    for file_name in tqdm(os.listdir(path)):
        #print(file_name)
        file_path = os.path.join(path, file_name)
        with fileinput.FileInput(file_path, encoding="utf-8", inplace=True) as file:
            #add sets with occur counts to per doc map
            occurences = dict()
            for [target, _] in ontology_set:
                occurences[target] = 0

            for line in file:
                line = compound_words_matcher(line, compounds_set)    
                for string in line.split():
                    
                    #replace with domain names before subbing "." etc because .NET and other similar cases
                    [result, match] = ontology_replace(string, ontology_set, simplify_set, occurences)                   
                    if match:
                        replaced_words_file.write(string + " = " + result +'\n')
                        string = result                        
                    
                    #remove extra: , . : ; ! ? / - [ ] ( )
                    string = re.sub("[,.:;'<>!?\/\-\[\]()\"]", ' ', string)

                    for word in string.split():

                        #remove numbers
                        word = re.sub("^[0-9]+$", '', word)
                   
                        #lemmatize words
                        word_type = det_type(word)                                   
                        word = lemmatizer.lemmatize(word.lower(), word_type)
                    
                        #replace with domain names again after lemmatization and re.sub because "kafka." would not get recognized
                        [result, match] = ontology_replace(word, ontology_set, simplify_set, occurences)
                        if match:
                            replaced_words_file.write(word + " = " + result +'\n')
                            word = result
                        print(word)
        file.close()
    replaced_words_file.close()             

if __name__ == "__main__":
    main()

