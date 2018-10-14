# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:01:22 2017

@author: cling
"""
def solve(N,D,K,S):
    MS = []
    for i in range(N):
        ms = D*1.0/((D-K[i])*1.0/S[i])        
        MS.append(ms)
    return min(MS)
            
def readintlst(line):
    st = line[:-1].split(' ')
    return map(int,st)

def main():
    fo = open('output.txt','w')
    with open('input.txt','r') as f:
        line = f.readline()
        T = int(line[:-1])
        for t in range(T):
            D,N = readintlst(f.readline())
            K = []
            S = []
            for i in range(N):
                k,s = readintlst(f.readline())
                K.append(k)
                S.append(s)
            speed = solve(N,D,K,S)
            fo.write('Case #%d: %.6f\n' % (t+1,speed))

    fo.close()
if __name__ == '__main__':
    main()