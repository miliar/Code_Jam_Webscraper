'''
Created on 2014-05-03

@author: Tiger
'''

import itertools
def getAns(A,B,K,case):
    solutions =0
    for x in range(A):
        for y in range(B):
            if x & y <K:
                solutions +=1
    print "Case #"+str(case)+": "+str(solutions)


f = open ("B-small-attempt0 (1).in","r")
case =1
tests = f.readline().strip()
for i in range(int(tests)):
    t = f.readline().strip().split()
    A= int(t[0])
    B=int(t[1])
    K=int(t[2])
    
    getAns(A,B,K,case)
    
    case+=1