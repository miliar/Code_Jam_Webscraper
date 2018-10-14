#!/usr/bin/python

import sys
import math

def isPalindrome(input):
    input=list(str(input))
    while len(input)>1:
        if input.pop(0)!=input.pop(-1):
            return False
    return True

def solve(input):
    a,b=map(int,input)
    count=0
    for v in range(math.ceil(math.sqrt(a)),
                   math.floor(math.sqrt(b))+1):
        count+=isPalindrome(v)*isPalindrome(v*v)
    return count

if __name__ == '__main__':
    with open(sys.argv[2], 'w') as out:
        with open(sys.argv[1]) as f:
            n = int(f.readline())
            for i, input in enumerate(f):
                input=input.strip().split()
                result=solve(input)
                print('Case #{}: {}'.format(i+1,result), file=out)
