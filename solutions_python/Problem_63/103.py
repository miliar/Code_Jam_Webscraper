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

def gettests(L, P, C):
    tests = scipy.logn(C,float(P)/L)
    
    num = scipy.log2(tests)
    if num%1.>0.:
      num +=1
    if num<0:
      num = 0.

    return long(num)

def prepare():
    file = open(sys.argv[1],'r')
    temp = file.readline()

    cases=1
    while cases>0:
        try:
            L, P, C = map(long,file.readline().split())
        except:
            cases=0
            break

        tests = gettests(L,P,C)
        print "Case #"+str(cases)+": "+str(tests)
        cases+=1

if __name__=='__main__':
    prepare()
