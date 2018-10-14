'''
Created on Apr 7, 2017

@author: fernandomendez
Tidy numbers
'''

import argparse
import sys
import math


def solve(line):
    dig = list(line)
    digval = [int(x) for x in dig]
    last_idx_greater = 0
    idx =0 
    still_Tidy =True
    while idx < len(digval) -1 and still_Tidy:
        if digval[idx] < digval[idx+1]:
            last_idx_greater = idx+1
        elif digval[idx] > digval[idx+1]:
            still_Tidy = False
        idx +=1
    if not still_Tidy:
        digval[last_idx_greater] -=1 
        for idx_corr in range(last_idx_greater+1, len(digval)):
            digval[idx_corr] =9
    while digval[0] ==0:
        digval.pop(0)
    return ''.join([str(x) for x in digval])


parser = argparse.ArgumentParser(description='''Template''',  epilog='')
parser.add_argument('input',  help='input file', )
parser.add_argument('output', help='output file')
args = parser.parse_args()

inFile = open (args.input)
outFile = open (args.output, 'w')
line = inFile.readline()
line= line.strip()
ncases = int(line)

for case in range(1, ncases+1):
    line = inFile.readline()
    line = line.strip()

    sol = solve(line)
    outFile.write('Case #'+str(case)+": "+str(sol)+"\n")
