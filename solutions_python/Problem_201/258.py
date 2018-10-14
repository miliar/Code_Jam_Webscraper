'''
Created on Apr 7, 2017

@author: fernandomendez
Bathroom Stalls
'''

import argparse
import sys
import math



def find_mami (nstall, npeop):
    if npeop == 1:
        return nstall/2, (nstall-1)/2

    lstall,hstall =  (nstall-1)/2, (nstall)/2
    if npeop %2 ==0:        # with the large
        return find_mami(hstall, npeop/2)
    elif npeop %2 ==1:        # with the small
        return find_mami(lstall, npeop/2)

def solve(line):
    N,K = [int(x) for x in line.split()]
    mami = find_mami(N,K)
    return ' '.join(str(x) for x in mami)

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
