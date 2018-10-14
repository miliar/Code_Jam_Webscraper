__author__ = 'zaeku'

import numpy as np
import time
start_time = time.time()

input_file = open('A-small-attempt0.in', 'r')
Test_data = input_file.readlines()[::-1]
input_file.close()
output_file = open('A-output.txt', 'w')

T = int(Test_data.pop().rstrip())
T_string = str(T)

for case in range(T):
    print("\nProgress : " + str(case+1) + " / " + T_string)
    output_file.write('Case #'+str(case+1)+': ')
    rt=map(int,Test_data.pop().rstrip().split())
    r = float(rt[0])
    t = float(rt[1])


    n = (1-2*r)/4 + np.sqrt( (2*r-1)**2 + 8*t)/4

    output_file.write(str(int(n)) + "\n")

output_file.close()
elapsed_time = time.time() - start_time
print "\nElapsed Time: "+str(elapsed_time)+"\nAverage Elapsed Time per case: "+str(elapsed_time/T)+"\n"

""" Area_1 =    r_n = r_1 + 2  Area = ((4*r+2)*n+2*n**2-n) -t == 0 """
"""    while ( Area <= t):
        Area += (2*r+1)
        r += 2
        Counter += 1  """
