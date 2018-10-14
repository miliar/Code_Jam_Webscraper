# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:58:09 2017

@author: root
"""
import numpy as np

def cut_array(ary):
    idx_false = np.where(ary == False)
    if(idx_false[0].size == 0):
        return ary
    idx_min = idx_false[0][0]
    ary = ary[idx_min:]
    return ary
    
def flip_next(erg):
    idx_false = np.where(erg == False)
    if(idx_false[0].size == 0):
        return erg
    
    idx_min = idx_false[0][0]
    if(idx_min + K > erg.size):
            return erg
    erg[idx_min:idx_min+K] = 1 - erg[idx_min:idx_min+K]
    flipcounts[it_in-1]+=1
        
    erg = cut_array(erg)
    erg = flip_next(erg)
    return erg
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#t = int(input())  # read a line with a single integer
#for i in range(1, t + 1):
#  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
#  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
filename = 'input.txt'
out_path = 'output.txt'
 
with open(filename, mode='r') as file: # b is important -> binary
    fileContent = file.readlines()
file.close()

number_tests = fileContent[0].split(' ')
number_tests = int(number_tests[0])
testcase_list = []
flipcounts = np.zeros(number_tests,dtype='int')
for it_in in range(1,number_tests+1):
    testcase_list.append(fileContent[it_in].split(' '))
    testcase_list[it_in-1][1] =testcase_list[it_in-1][1].rstrip('\n')

    
    b = testcase_list[it_in-1][0]
    K = int(testcase_list[it_in-1][1])
    b = b.replace('+','1 ')
    b = b.replace('-','0 ')
    a = np.matrix(b, dtype='bool')
    a = np.array(a)
    erg = a[0]
    
    
    erg = cut_array(erg)
    erg = flip_next(erg)
    if np.any(erg == False):
        flipcounts[it_in-1] = -1
        


fo = open(out_path, "w")

#size_final = len(final_map)
#fo.write(str(size_final) + "\n")

for it in range(1,number_tests+1):
    if flipcounts[it-1] < 0:
        str_tmp = "Case #{}: {}".format(it, 'IMPOSSIBLE')
    else:
        str_tmp = "Case #{}: {}".format(it, flipcounts[it-1])
        
    
#    str_tmp = str(it) + " " + str(list(set(final_map[it])))
#    str_tmp = str_tmp.replace('[', '')
#    str_tmp = str_tmp.replace(']', '')
#    str_tmp = str_tmp.replace(',', '')
    
    fo.write(str_tmp + '\n')
fo.close()