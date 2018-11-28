#!/usr/bin/env python
'''
      
'''

import sys
from pprint import pprint
import string

d = {} 

combinations = {1:1, 2:1, 3:3, 4:6, 5:10, 6:15, 7:12 } 


def generate_recycled_nums(str_num):
    l = list() 
    for i in xrange(0,len(str_num)):
        num = str_num[i:]+str_num[:i]
        if not num.startswith('0') and int(num) not in l:
            l.append(int(num))
    return l 

def do_one_case(csn, A, B):
    tot_rnums = 0
    memory_set = set()
    for i in xrange(A, B+1):
        #if i % 10000 == 0 : print i
        if i < 10: continue 
        if i in memory_set: continue
        rec_nums = generate_recycled_nums(str(i))
        rec_list = [j for j in rec_nums if A <= j <= B]
        if len(rec_list) >= 2:
            tot_rnums += combinations[len(rec_list)]
            for num in rec_list:
                memory_set.add(num)

    print "Case #"+str(csn)+":", tot_rnums 

def main():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        A, B = sys.stdin.readline().strip().split()
        #print W,H,T
        do_one_case(i+1, int(A), int(B))


if __name__ == "__main__":
    main()
