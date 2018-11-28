#!/usr/bin/python

import re
import sys
from math import ceil, floor, sqrt

input_file = open('C-large-1.in')
output_file = open('C-large-1.out', 'w')

T = int(input_file.readline())

def fair(n):
    tmp = 0;
    i = n
    while i > 0:
        tmp *= 10
        tmp += i % 10
        i /= 10
    return tmp == n

def rec(s, A, B):
    global nums
    if len(s)> len(str(B)): return;
    if len(s) > 0 and s[0] != '0':
        n = int(s)
        if (n >= A and n <= B):
            nums.append(n)  
    rec('0'+s+'0', A, B)
    rec('1'+s+'1', A, B)
    rec('2'+s+'2', A, B)

nums = []

def fairnumbers(A, B):
    global nums
    nums = []
    rec('', A, B)
    rec('0', A, B)
    rec('1', A, B)
    rec('2', A, B)
    if 3 in xrange(A, B+1): nums.append(3)
    return nums

for t in range(T):
    A, B = map(int, input_file.readline().split(' '))

    sum = 0
    for i in fairnumbers(int(floor(sqrt(A))), int(ceil(sqrt(B)))+1):
        sq = i*i
#        print i, fair(i), sq, fair(sq)
        if fair(i) and fair(sq) and sq >= A and sq <= B:
            sum += 1

    output_file.write("Case #" + str(t + 1) + ": " + str(sum) + "\n")
        

input_file.close()
output_file.close()
