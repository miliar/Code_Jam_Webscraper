"""
Google Code Jam        
"""

import sys

name="B-small-attempt1"
DBG=0
DBN=5

def allok(L,n):
    for i in L:
        if i < n:
            return True
    return False

with open(name+'.in','r') as infile:
    cases = int(infile.readline())
    with open(name+'.out','w') as outfile:
        for i in range(1,cases+1):
            
            # parse input
            P = int(infile.readline())
            M = tuple(map(int,infile.readline().split(' ')))
            T=[]
            ans=0#(1<<P)-1
            for j in range(P):
                T.append(tuple(map(int,infile.readline().split(' '))))
            for j in range(P):
                for k in tuple(zip(*[iter(M)]*(1<<P-j))):
                    ans+=allok(k,P-j)

            # coding here:
            
            # output the answers
            print('Case #%d:'%i,ans,file=sys.stdout if DBG else outfile)

