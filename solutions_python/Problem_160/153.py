
#!/usr/bin/python

import sys
import os
from collections import defaultdict, Counter
import numpy as np

results = dict()


def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(*args):
    return reduce(lcm, args)



def haircut_OLD(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        B, N = map(int, input_file.readline().strip().split())
        all_mis = map(int, input_file.readline().strip().split())
        B_idx = -1
        print(i)
        #remain_time = [0]*B

        all_lcm = lcmm(*all_mis)
        cust_per_lcm = sum(map(lambda x: all_lcm/x, all_mis))
        N = N % cust_per_lcm
        if N == 0:
            N = cust_per_lcm
        print(N)

        all_mis_array = np.array(all_mis)
        remain_time = np.zeros(B, dtype=int)
        dec_array = np.ones(B, dtype=int)
        while True: #N > 0:
            #print(N)
            ready_barber = np.where(remain_time == 0)[0]
            if N <= len(ready_barber):
                B_idx = ready_barber[N-1]
                break
            N -= len(ready_barber)
            remain_time[ready_barber] = all_mis_array[ready_barber]
            remain_time -= dec_array * np.min(remain_time)

        results[i+1] = B_idx+1
    input_file.close()



def haircut_NEW(input_filename):
    input_file = open(input_filename, "r")
    num_test_cases = int(input_file.readline().strip())
    for i in xrange(num_test_cases):
        B, N = map(int, input_file.readline().strip().split())
        all_mis = map(int, input_file.readline().strip().split())
        B_idx = -1
        print(i)
        #remain_time = [0]*B
        #print("  "+str(N)+" "+str(B))
        all_lcm = lcmm(*all_mis)
        cust_per_lcm = sum(map(lambda x: all_lcm/x, all_mis))
        N = N % cust_per_lcm
        if N == 0:
            N = cust_per_lcm
        #print("  "+str(N)+" "+str(B))
        #print("  "+str(all_mis))

        all_mis_array = np.array(all_mis)
        remain_time = np.zeros(B, dtype=int)
        dec_array = np.ones(B, dtype=int)
        max_mi = np.max(all_mis_array)
        pass_flag = False
        while True: #N > 0:
            #print("  "+str(N)+" "+str(remain_time)+" "+str(pass_flag))
            #print("  "+str(N)+" "+str(B))
            if not pass_flag: #N > B:
                remain_time_neg = (remain_time - max_mi*10)
                if len(np.where(remain_time_neg > 0)[0]) != 0:
                    raise Exception(str(remain_time)+" "+str(all_mis_array))
                dec_amount = abs(sum((remain_time_neg) / all_mis_array))
                if dec_amount >= N:
                    pass_flag = True
                    continue
                else:
                    N -= dec_amount
                    remain_time = remain_time_neg % all_mis_array
            else:
                #print(N)
                ready_barber = np.where(remain_time == 0)[0]
                if N <= len(ready_barber):
                    B_idx = ready_barber[N-1]
                    break
                N -= len(ready_barber)
                remain_time[ready_barber] = all_mis_array[ready_barber]
                remain_time -= dec_array * np.min(remain_time)

        results[i+1] = B_idx+1
        #print (B_idx+1)
        #if i+1 == 8: break
    input_file.close()




def write_output():
    output_file = open("output.txt", "w")
    for k,v in results.iteritems():
        output_file.write("Case #"+str(k)+": "+str(v)+"\n")
    output_file.close()


if __name__ == "__main__":
    input_filename = sys.argv[1]
    haircut_NEW(input_filename)
    write_output()

#
