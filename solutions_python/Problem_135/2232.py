import numpy as np
import re

filename = open('A-small-attempt0.in', 'r')

test_case_number = filename.readline()

for i in range(int(test_case_number)):
    i = i + 1
    the_chosen_ones = []
    for j in range(2):
        the_matrix = []    
        row_chosen1 = filename.readline()
        row11 = filename.readline().strip().split()
        row12 = filename.readline().strip().split()
        row13 = filename.readline().strip().split()
        row14 = filename.readline().strip().split()
        the_matrix.append(row11)
        the_matrix.append(row12)
        the_matrix.append(row13)
        the_matrix.append(row14)
        the_chosen_ones.append(the_matrix[int(row_chosen1)-1])
    the_real_chosen_ones = []
    for k in range(4):
        for t in range(4):
            if the_chosen_ones[0][k] == the_chosen_ones[1][t]:
                the_real_chosen_ones.append(the_chosen_ones[0][k])
            else:
                continue

    if len(the_real_chosen_ones) > 1:
        print 'Case #%s:' %  ( i ), 'Bad magician!'
    elif len(the_real_chosen_ones) == 1:
        print 'Case #%s:' % ( i ), the_real_chosen_ones[0]
    elif len(the_real_chosen_ones) == 0:
        print 'Case #%s:' % ( i ), 'Volunteer cheated!'
            
