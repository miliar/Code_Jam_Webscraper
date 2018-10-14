#!/usr/bin/python

import os
import sys
import math
def comb(n, k):
    if n < k or k < 0 or n < 0:
        return 0
    elif n == k or k == 0:
        return 1
    else:
        return math.factorial(n) / math.factorial(k) / math.factorial(n - k)


class pu():
    def __init__(self):
        self.all_case = []
        self.all_case.append([0])
        self.all_case.append([0, 0])
        case = [0, 1]  # line 2 : case 2
        self.all_case.append(case[:])
        case = [0, 1, 1]  #line 1 : case 3
        self.all_case.append(case[:])
        #print self.all_case
        #print '-------'
    def update(self, n):
        #print "update", n, len(self.all_case)
        first =  len(self.all_case) 
        for k in range(first, n + 1):
            list_k = [0, 1, 1]
            for length in range(3, k):
                this_num = 0
                for next_length in range(1, length):
                    this_num += self.all_case[length][next_length] * comb(k - length - 1, length - next_length - 1)
                    #print k, length, next_length, '-',
                    #print k - length - 1, length - next_length - 1, comb(k - length - 1, length - next_length - 1), self.all_case[length][next_length]
                list_k.append(this_num + 0)
            self.all_case.append(list_k)    
    def access(self, n):
        if n > len(self.all_case) - 1:
            self.update(n)
        #print self.all_case
        return sum(self.all_case[n])

infile = open(sys.argv[1])
line_num = int(infile.readline())

pure = pu()

for i in range(line_num):
    n = int(infile.readline())
    x = pure.access(n)
    print 'Case #' + str(i+1) + ':', x % 100003

for l in pure.all_case:
    #print l
    None
