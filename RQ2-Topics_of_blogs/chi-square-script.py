# August 2022

from scipy.stats import chi2_contingency
import numpy as np

# To run this file:
# 1. de-comment the data you choose to test
# 2. copy and paste the data matrix to line 174
# 3. change the total_sum amount on line 206 depending on which data you are testing

########################################
# Data for type vs topic:
########################################

# data = np.array(
    # [
        # [29,	6,	17,	34,	24],
        # [19,	6,	5,	22,	11],
        # [12,	5,	9,	9,	4],
        # [8,	1,	9,	7,	5],
        # [1,	0,	1,	4,	1],
        # [0,	0,	1,	2,	3],
        # [0,	0,	0,	0,	1]
    # ])

########################################
# Data for LDA topics vs Qualitative topics:
########################################

data = np.array(
   [
   [4, 13, 5, 5,0], 
   [ 43, 46 , 37 , 15 ,  4 ],
   [30, 18, 2, 33 ,  0 ],
   [ 30, 38 , 10 , 7 ,  5 ],
   [ 5, 16, 18, 17,  49],
   [6, 36, 20, 39, 14],
   [ 0, 2 , 7 , 6 ,  1 ]
   ] )

########################################
# Data for LDA topics vs Type:
########################################

# data = np.array(
   # [
   # [2, 14, 3, 1, 4, 0], 
   # [ 21, 79 , 18 , 20 ,  4, 0],
   # [2, 36, 6, 19 ,  9, 2 ],
   # [ 1, 33 , 19 , 33 ,  3, 6 ],
   # [ 35, 33, 12, 15,  2, 1],
   # [23, 40, 8, 40, 0, 0],
   # [ 10, 3 , 1 , 5 ,  0, 0 ]
   # ] )

########################################
# Data for Qualitative topics vs Type:
########################################

# data = np.array(
   # [
   # [5, 56, 19, 21, 5, 2], 
   # [ 23, 61 , 15 , 51 ,  6, 3],
   # [17, 47, 12, 16 ,  3, 1 ],
   # [ 22, 47 , 14 , 23 ,  6, 0 ],
   # [ 26, 19 , 3 , 16 ,  2, 0 ]
   # ] )

########################################
# Data for Task vs Type:
########################################

#data = np.array(
#    [
#    [43, 72, 50, 14, 23, 25], 
#    [ 1, 2 , 3 , 0 ,  3, 5 ],
#    [18, 16, 10, 4 ,  4, 5 ],
#    [ 4, 1 , 1 , 0 ,  0, 0 ],
#    [ 4, 21, 11, 14,  7, 23],
#    [27, 27, 18, 26, 12, 10],
#    [ 3, 0 , 0 , 0 ,  0, 0 ]
#    ] )

########################################
# Data for Task vs Type: 3 steps in ADD model
########################################

#data = np.array(
#   [
#      [ 115,	64,	48],
#      [ 3,	3,	8],
#      [ 34,	14,	9],
#      [ 5,	1,	0],
#      [ 25,	25,	30],
#      [ 54,	44,	22],
#      [ 3,	0,	0]
#    ] )

########################################
# Code-co-occurence values
########################################

#data = np.array(
#    [
#    [1,2,0,0,0,0,1,0,3,1,2,0,0],
#    [1,4,1,1,2,2,3,1,17,10,5,0,0],
#    [14,6,19,4,6,2,14,8,21,10,0,5,2],
#    [7,16,19,5,2,7,7,27,107,0,10,10,1],
#    [3,26,5,16,5,12,18,8,0,107,21,17,3],
#    [2,5,0,1,1,0,1,0,8,27,8,1,0],
#    [1,12,2,79,0,2,0,1,18,7,14,3,1],
#    [1,9,0,68,0,0,2,0,12,7,2,2,0],
#    [0,0,1,0,0,0,0,1,5,2,6,2,0],
#    [1,6,0,0,0,68,79,1,16,5,4,1,0],
#    [21,18,0,0,1,0,2,0,5,19,19,1,0],
#    [14,0,18,6,0,9,12,5,26,16,6,4,2],
#    [0,14,21,1,0,1,1,2,3,7,14,1,1],
#    ])

########################################
# AK vs type data:
########################################

#data = np.array(
#    [
#        [7.461538462,	4.5,	9,	12.8,	17],
#        [4.846153846,	3.5,	6.666666667,	9.2,	15],
#        [3.384615385,	1,	2.666666667,	3.4,	7.222222222],
#        [4.692307692,	7.5,	3.5,	1.8,	3.666666667],
#        [2.538461538,	0.5,	2,	4.2,	5.444444444],
#        [1.461538462,	3.5,	2.166666667,	3.2,	4],
#        [1.769230769,	0,	1.833333333,	2.2,	4.888888889],
#        [3.538461538,	2.5,	1.166666667,	1.4,	2.555555556],
#        [3.307692308,	0,	0.8333333333,	1.6,	3.222222222],
#        [3,	1,	2.5,	1,	2.444444444],
#        [0.6923076923,	0.5,	3,	3.4,	4.111111111],
#        [1.153846154,	0,	1.5,	3.2,	0.8888888889],
#        [1,	0,	0.1666666667,	2.4,	0.3333333333    ]
#    ] )   

########################################
# AK vs topic data:
########################################

#data = np.array(
#    [
#        [12,	4.666666667,	13,	12.81818182,	5.2],
#        [10.08333333,	8.666666667,	12.25,	7.545454545,	2.4],
#        [3.833333333,	1.666666667,	8.25,	4.818181818,	1.4],
#        [3,	7,	1,	5.818181818,	2.8],
#        [3.916666667,	1,	7,	2.818181818,	1.4],
#        [3.416666667,	1.333333333,	2,	3.090909091,	0.8],
#        [2.666666667,	1,	6.5,	2.090909091,	1],
#        [1.666666667,	2,	1,	3.636363636,	3.6],
#        [1,	0.3333333333,	2.25,	4.909090909,	1.8],
#        [1.75,	4.666666667,	1.25,	2.272727273,	3.6],
#        [2.416666667,	2.666666667,	5,	1.545454545,	1.6],
#        [2.083333333,	1.333333333,	0.25,	1.181818182,	1],
#        [2,	0,	0,	0.3636363636,	0.2    ]
#    ] )   

########################################
# Code:
########################################

answer = data
# change row and col values depending on data used
for row in range(0,7,1):
    for col in range(0,5,1):
        
        # for some reason the data values change each iteration, so reset them each loop 
        
        data = np.array(
        [
        [4, 13, 5, 5,0], 
        [ 43, 46 , 37 , 15 ,  4 ],
        [30, 18, 2, 33 ,  0 ],
        [ 30, 38 , 10 , 7 ,  5 ],
        [ 5, 16, 18, 17,  49],
        [6, 36, 20, 39, 14],
        [ 0, 2 , 7 , 6 ,  1 ]
        ] )
        
        # get the 4 values for the contingency table (2x2 matrix):
        # [current, right],
        # [bottom, bottom_right]
        
        current = data[row,col]
        row_sum = sum(data[row])
        col_sum = sum(data[:,col])
        right = row_sum-current
        bottom = col_sum-current
        
        # total_sum values change depending on data used:
        # type vs task total = 507
        # tye vs task steps = 507
        # code co-occurence total = 1392
        # AK vs type = 220.9239316
        # AK vs topic = 225.6257576
        # type vs topic = 256
        # LDA topics vs type = 563
        # Qualitative topics vs type = 541
        # LDA topics vs qualitative topics = 581
        
        total_sum = 581
        bottom_right = total_sum-row_sum-col_sum+current
        
        # create table for each co-occurence
        contingency_table = np.array(
            [
                [current, right],
                [bottom, bottom_right]
            ])
        stat, p, dof, expected  = chi2_contingency(contingency_table)
        
        # create table of all co-occurences
        answer[row,col] = stat
        
        # print each contingency table and chi2 stat for each data item
        print(contingency_table)
        print(np.round(stat,2)) # rounded to two decimal places

# final chi2 matrix:
print(answer) # rounded to nearest whole number
