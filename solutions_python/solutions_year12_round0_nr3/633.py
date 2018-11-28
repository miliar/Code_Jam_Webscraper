#! /usr/bin/env python

# Recycled Numbers
# Code Jam 2012 Round 1 - Problem C
# Mark Sherman brazentone@gmail.com

import sys


# Does the actual work solving the problem
def do_case(case_num):
    line = fin.readline().split()
    a = int(line[0]) # low bound
    b = int(line[1]) # high bound
    length = len(str(a)) # how many digits the numbers are
    count = 0
    
    for i in range( a , b ):
        num = i
        for j in range(length-1):
            num = rotate(num, length)
            if num == i:
                break
            if num > i and num <= b :
                count = count + 1
    
    fout.write( "Case #" + str(case_num) + ": " + str(count) + '\n' )

def rotate(num, length):
    digit = num % 10
    num = (num / 10) + ( digit * 10 ** (length-1) )
    return num


######################################################
# Setup stuff

OUTFILE = 'outfile'
    
fin = open(sys.argv[1], 'r')

if len(sys.argv) > 2:
    outf = sys.argv[2]
else:
    outf = OUTFILE
    
fout = open(outf, 'w')

CASES = int(fin.readline()) 

for i in range(CASES):
    do_case(i+1)
    
    