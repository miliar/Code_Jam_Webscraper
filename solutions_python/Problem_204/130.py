# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:01:22 2017

@author: cling
"""
import math
def fetchlst(S,t):
    lst = []
    for i in range(len(S)):
        lst.append(S[i][t[i]])
    return lst

def checkit(S,t,mult):
    for i in range(len(S)):
        now = S[i][t[i]]
        if now<mult*0.9 or now>mult*1.1:
            return False
    return True

def locateminimalmult(now):
    minmult = math.ceil(now/1.1)
    if now>minmult*1.1:
        return -1
    else:
        return minmult

def findcurrentmax(S,t):
    m = -1
    mi = -1
    for i in range(len(S)):
        if S[i][t[i]]>m:
            m = S[i][t[i]]
            mi = i
    return m,mi
    
def proceedpointer(S,t,mult):
    N = len(S)
    P = len(S[0])
    flag = True
    for i in range(N):
        while t[i]<P and S[i][t[i]]<mult*0.9:
            t[i]+=1
        if t[i]==P:
            flag = False
    return flag

def solve(N,P,R,S):
    for i in range(N):
        S[i] = map(lambda x: x*1.0/R[i],sorted(S[i]))
#    print S
    t = [0]*N
    total = 0
    flag = True
    while flag:
        now,i = findcurrentmax(S,t)        
        mult = locateminimalmult(now)
#        print mult,fetchlst(S,t)        
        if mult==-1:
            t[i]+=1
            if t[i]==P:
                flag = False
                break
            continue
        
        flag = proceedpointer(S,t,mult)
#        print flag        
#        print mult,fetchlst(S,t)        
        if not flag:
            break
        else:
            ok = checkit(S,t,mult)
#            print ok
            if ok:
                total += 1
                t = map(lambda x: x+1,t)
            if any(map(lambda x: x==P,t)):
                flag = False
    return total
        
def readintlst(line):
    st = line[:-1].split(' ')
    return map(int,st)
def main():
    fo = open('output.txt','w')
    with open('input.txt','r') as f:
        line = f.readline()
        T = int(line[:-1])
        for t in range(T):
            N,P = readintlst(f.readline())
            R = readintlst(f.readline())
            S = []
            for i in range(N):
                S.append(readintlst(f.readline()))

            total = solve(N,P,R,S)
            fo.write('Case #%d: %d\n' % (t+1,total))

    fo.close()
if __name__ == '__main__':
    main()