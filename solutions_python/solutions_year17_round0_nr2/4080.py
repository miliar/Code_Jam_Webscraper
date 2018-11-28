# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:24:18 2017

@author: Joonhahn
"""


def list_to_int(this_n):
    this_int = ''
    for dig in this_n:
        this_int = this_int+dig
    return int(this_int)

import fileinput
f = fileinput.input(r'B-large.in')
fo = open(r'B-large.out', 'w')
try :
    T = int(f.readline().strip())
    for i in range(T):
        this_n = list(str(f.readline().strip()))
        if len(this_n) == 1 :
            #print 'Case #{0}: {1}'.format(i+1, list_to_int(this_n))
            fo.write('Case #{0}: {1}'.format(i+1, list_to_int(this_n)) + '\n')
            
        else :
            diff_list = [int(this_n[idx+1])-int(this_n[idx]) for idx in range(len(this_n)-1)]
            k = len(this_n) - 1
            for j in range(len(diff_list)-1,-1,-1):
                #print this_n, j, k
                #print diff_list,j,k
                if diff_list[j] < 0 :
                    this_n = list(str(list_to_int(this_n) - (list_to_int(this_n[j+1:])+1)))
                    diff_list = [int(this_n[idx+1])-int(this_n[idx]) for idx in range(len(this_n)-1)]
                    k = j
    
                         
            #print 'Case #{0}: {1}'.format(i+1, list_to_int(this_n))
            fo.write('Case #{0}: {1}'.format(i+1, list_to_int(this_n)) + '\n')
finally:
    f.close()
    fo.close()
