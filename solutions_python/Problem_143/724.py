# New Lottery Game 

import math
import time

time_start = time.time()

file_input = open('B-small-attempt0.in')
##file_out = open('output_2.txt','w')
##file_out.write('')
##file_out.close()

Test_Cases = [int(a) for a in file_input.readline().split(' ')][0]
print(Test_Cases)
N = 1

while N <= Test_Cases:
    win_counts = 0

    row1 = [int(a) for a in file_input.readline().split(' ')]
    
    A = row1[0]
    B = row1[1]
    K = row1[2]

    for i in range(0,A):

        for j in range(0,B):

            Winner = i&j

            if Winner < K:

                win_counts +=1
                
##    file_out = open('output_2.txt','a')
##    file_out.write('Case #'+str(N)+': '+str(win_counts)+'\n')
##    file_out.close

    print('Case #'+str(N)+': '+str(win_counts))

    N+=1

time_end = time.time()

print('Time taken is: '+str(time_end-time_start)+' sec')
