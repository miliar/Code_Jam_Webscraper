# encoding: UTF-8

from __future__ import absolute_import, division

import collections
import itertools
import sys

class gcj:
    IN = open('D:\code jam\input.in', 'r')
    OUT = open('D:\code jam\output.txt', 'w')
    buf = None

    identity = lambda x: x

    @classmethod
    def _read_line(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = None
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def line(cls, conv=identity):
        line = cls._read_line()
        return conv(line.rstrip(b'\r\n'))

    @classmethod
    def splitline(cls, conv=identity):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line()
            i = 0
            l = len(line)
            while i < l and line[i].isspace():
                i += 1
            line = line[i:]
        cls.buf = line

    @classmethod
    def token(cls, conv=identity):
        cls.whitespace()
        line = cls._read_line()
        i = 0
        l = len(line)
        while i < l and not line[i].isspace():
            i += 1
        cls.buf = line[i:] if i < l else None
        return conv(line[:i])

    @classmethod
    def tokens(cls, cnt, conv=identity):
        #tokens=[]
        #for _ in range(cnt):
        #    tokens.append(cls.token(conv))
        #return tokens   
        return [cls.token(conv) for _ in range(cnt)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return 'Case #{}:'.format(cls.current_case)
    
    @classmethod
    def writefile(cls, case, solve):
        cls.OUT.write( case + " " + str(solve) + '\n')
        return
    

def solve():
    #Get Variables
    N = gcj.token(int) #can be token(int) or tokens(N, int) # can be int or str
    print('N:', N)
    N=str(N)
    N=list(N)
    i=0
    while(i<len(N)):
        N[i]=int(N[i])
        i+=1
        
    #print('N:', N)
    #print('len_S:', len(N)) 

    i=0
    while(i<len(N)-1):
        if(N[i]<=N[i+1]):
            i+=1
        else:
            #backtrack until the first of the series and reduce 1 all forward become 9
            while i>0 and N[i]==N[i-1]:
                i-=1
            
            N[i]-=1
            i+=1
            while i<len(N):
                N[i]=9
                i+=1
            #print('N:', N)
            break
                
    #print('N:', N)
    if(N[0]==0):
        N=N[1:]
        
    result = ''.join(str(e) for e in N)
    #print('B:', B)    
    #print('K:', K)    

        
    return result

def _solve(A,B,K):
    
    #contar at� min(A,K)
    x = min (A,K)
    partial = x*(x-1) #j� multipliquei por 2
    
    if (K<A):
        #COUNT ALL between K and A (MULTIPLICAR POR 2)
        
        #till k I can add again 0 a K e K a A = K*(A-K)*2
        partial+=K*(A-K)*2
        
        i=K
        while(i<A):
            j=i+1
            while (j<A):
                if (j&i < K):
                    partial+=2
                j+=1
            i+=1
        
    if (K>A):
        #COUNT ALL between A and min(K,B) - square A : min(K,B)-A 
        y = min(K,B)
        partial += A * (y-A)
        
    if (K<B):
        #COUNT ALL between max(K,A) and B
        y= max(K,A)
        
        #till K I can add again 0 to K and y to B => K*(B-y)
        partial+=min(K,A)*(B-y)
        
        i=y
        while(i<B):
            j=K
            while (j<A):
                if (j&i < K):
                    partial+=1
                j+=1
            i+=1
        
    return partial

def main():
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        if case == "Case #34:":
            j=1
        result = solve()
        
        gcj.writefile(case, result)
        print(case, result)

main()
