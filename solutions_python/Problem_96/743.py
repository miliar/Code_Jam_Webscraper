'''
Google Code Jam 2012, Qualification Round
Problem B
Created on Apr 13, 2012

@author: Gabriel D. Holodak
'''
import math
fin = open('B-large.in')
fout = open('output.txt', 'w')
num_cases = int(fin.readline().strip())

for i in range(num_cases):
    output_string = 'Case #' + str(i + 1) + ": "
    print output_string
    numbers = fin.readline().strip().split()
    num_googlers = int(numbers[0])
    num_surprising = int(numbers[1])
    p = int(numbers[2])
    #print 'p =',p
    current_index = 3
    max_googlers = 0
    while current_index - 3 < num_googlers and num_surprising > -1:
        
        current_score = int(numbers[current_index])
        if p==0:
            max_googlers+=1
            #print 'p = 0, all scores automatically qualify'
        elif current_score / p >= 3 or (current_score / p == 2 and p-(current_score % p) < 3):
            max_googlers += 1
            #print 'current score =', str(current_score), ', not surprising' 
        elif current_score!= 0 and num_surprising > 0 and (current_score / 3 == (p - 1) or (current_score / 3 == (p - 2) and current_score % 3 == 2)):
            max_googlers += 1
            num_surprising -= 1
            #print 'current score =', str(current_score), ', surprising,', num_surprising, 'surprising left'
        current_index += 1
    fout.write(output_string + str(max_googlers) + '\n')
fout.close()
fin.close()
