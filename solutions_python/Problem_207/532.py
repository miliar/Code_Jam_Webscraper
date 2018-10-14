# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:01:22 2017

@author: cling
"""
import numpy

def genseqxxx(x):
    return [0,1,2]*x
    
def genseqxx0(x):
    return [0,1]*x

def genseqx0z(x):
    return [0,2]*x
    
def genseqxxz(C):
    if C[1]==C[2]:
        seq = genseqxxx(C[1])
    else:
        seq = genseqxxx(C[2]) + genseqxx0(C[1]-C[2])
    return seq
    
def solve(N,R,O,Y,G,B,V):
    more = max(R,Y,B)
    less = N-more
    if more>less:
        return 'IMPOSSIBLE'
    C = [R,Y,B]
    Lo = 'RYB'
    lst = numpy.argsort(C)
    lst = lst[::-1]
    print lst
    L = ''
    for i in range(3):
        L += Lo[lst[i]]
    C = sorted(C)
    C = C[::-1]
    if C[0]>C[1]:
        x = C[0]-C[1]
        seq = genseqx0z(x) + genseqxxz([C[0]-x,C[1],C[2]-x])
    else:
        seq = genseqxxz(C)
    seq = ''.join(map(lambda x: L[x],seq))
    return seq
            
def readintlst(line):
    st = line[:-1].split(' ')
    return map(int,st)

def main():
    fo = open('output.txt','w')
    with open('input.txt','r') as f:
        line = f.readline()
        T = int(line[:-1])
        for t in range(T):
            N,R,O,Y,G,B,V = readintlst(f.readline())
            ansstr = solve(N,R,O,Y,G,B,V)
            fo.write('Case #%d: %s\n' % (t+1,ansstr))

    fo.close()
if __name__ == '__main__':
    main()