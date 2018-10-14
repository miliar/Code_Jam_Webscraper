'''
Created on Sep 3, 2009

@author: gatanov
'''
from numpy import *


def count(str,substr = "welcome to code jam"):
    num = zeros((len(str) + 1,len(substr) + 1),dtype = int)
    num[:,0] = 1
    for pos in range(1,len(str) + 1):
        for c in range(1,len(substr) + 1):
            if (str[pos - 1] == substr[c - 1]):
                num[pos,c] = (num[pos - 1,c] + num[pos - 1,c - 1]) % 10000
            else:
                num[pos,c] = num[pos - 1,c]
    return num[-1,-1]


if __name__ == '__main__':
    N = int(raw_input())
    for case in range(1,N+1):
        print "Case #%d: %04d" % (case,count(raw_input()))