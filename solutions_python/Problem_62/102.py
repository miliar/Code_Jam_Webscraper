#!/usr/bin/python
"""
Usage:
  ./solution.py test.in > test.out

Used libraries:
- scipy
"""
import scipy
import pdb
import sys

def getcrossings(lines):
    lines.sort()
    sortel = scipy.array(lines)
    crossovers = 0
    for i in range(scipy.shape(sortel)[0]):
        crossovers += scipy.where(sortel[i+1:,1]<sortel[i,1],1,0).sum() \
                    +scipy.where(sortel[:i,1]>sortel[i,1],1,0).sum()

    return crossovers/2


def prepare():
    file = open(sys.argv[1],'r')
    temp = file.readline()

    cases=1
    while cases>0:
        try:
            number = map(int,file.readline().split())[0]
        except:
            cases=0
            break
        lines = [tuple(map(int,file.readline().split())) for i in range(number)]
        crossovers = getcrossings(lines)
        print "Case #"+str(cases)+": "+str(crossovers)
        cases+=1

if __name__=='__main__':
    prepare()
