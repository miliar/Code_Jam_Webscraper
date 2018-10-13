# Magic Trick - Short

import math
import time

time_start = time.time()

file_input = open('A-small-attempt0.in')
file_out = open('output_1.txt','w')
file_out.write('')
file_out.close()

Test_Cases = [int(a) for a in file_input.readline().split(' ')][0]

N = 1

while N <= Test_Cases:

    row1 = [int(a) for a in file_input.readline().split(' ')][0]

    layout1 = []
    for i in range(4):
        layout1.append([int(a) for a in file_input.readline().split(' ')])

    answer1 = layout1[row1-1]

    row2 = [int(a) for a in file_input.readline().split(' ')][0]

    layout2 = []
    
    for i in range(4):
        layout2.append([int(a) for a in file_input.readline().split(' ')])

    answer2 = layout2[row2-1]

    answers = list(set(answer1) & set(answer2))

    answer_length = len(answers)

    if answer_length == 1:
        
        file_out = open('output_1.txt','a')
        file_out.write('Case #'+str(N)+': '+str(answers[0])+'\n')
        file_out.close()

    elif answer_length > 1:

        file_out = open('output_1.txt','a')
        file_out.write('Case #'+str(N)+': Bad magician!\n')
        file_out.close()

    else:

        file_out = open('output_1.txt','a')
        file_out.write('Case #'+str(N)+': Volunteer cheated!\n')
        file_out.close()

    N+=1


