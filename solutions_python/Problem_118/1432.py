#!/usr/bin/env python
#By Jai Dhyani    

# usage: solution.py input_file
# prints solution to stdout
 
import sys
from math import sqrt
 
def list_to_int(l):
    return int(''.join(str(c) for c in l))

def count_palindromes(a,b):
    a,b=min(a,b),max(a,b)
    lower_ten=len(str(a))+1
    upper_ten=len(str(b))-1
    count=sum([9*pow(10,(l-1)/2) for l in xrange(lower_ten,upper_ten+1)])
    a_digits=[int(d) for d in str(a)]
    a_half=(len(a_digits)+1)/2
    for i,d in enumerate(a_digits[:a_half]):
        count+=((9-d)*pow(10,a_half-i-1))
    if list_to_int(a_digits[a_half::-1]) >= list_to_int(a_digits[-a_half:]):
        count+=1
    b_digits=[int(d) for d in str(b)]
    b_half=(len(b_digits)+1)/2
    for i,d in enumerate(b_digits[:b_half]):
        count+=((d-1)*pow(10,b_half-i-1))
    if list_to_int(b_digits[b_half::-1]) >= list_to_int(b_digits[-b_half:]):
        count+=1
    print count

def solve( x ):
    return 0

def readints(f):
    return [int(x) for x in f.readline().split()]

def readtext(f):
    return f.readline()[:-1]

readtrial = readtext

def list_to_int(n):
    return int(''.join(map(str,n)))

def next_nice_root(n):
    digits=[int(d) for d in str(n)]
    half=digits[:(len(digits)+1)/2]
    if len(digits)%2==0:
        if digits[0]==2:
            return list_to_int([1]+[0]*(len(digits)-1)+[1])
        if sum(half)==4:
            if digits[:4]==[1,1,1,1]:
                return list_to_int([2]+[0]*(len(digits)-2)+[2])
        


"""
def get_nice_roots():
    start=[1,2,3,11,22,101,111,121,202,212,1001,1111,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002]
    for x in start:
        yield x
    h=3
    even=True
    while True:
"""

def readtrial(f):
    niceroots=[1,2,3,11,22,101,111,121,202,212,1001,1111,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002]
    lower,upper=readints(f)
    lower_root=sqrt(lower)
    upper_root=sqrt(upper)
    fscount=0
    for n in niceroots:
        if n>upper_root:
            break
        if n>=lower_root:
            fscount+=1
    return fscount

if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename)
    try:
        numtrials = readints(f)[0]
    except IndexError as ie:
        print 'no input data in %s'%filename
        exit(0)
    for i in xrange(numtrials):
        answer = readtrial(f)
        answer_str = "Case #%d: %s"%(i+1,str(answer))
        print answer_str
