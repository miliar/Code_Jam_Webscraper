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
    S = gcj.token(str) #can be token(int) or tokens(N, int) # can be int or str
    K = gcj.token(int)

    
    print('K:', K)   
    print('len_S:', len(S)) 

    S=list(S)
    print('S:', S)  

    j=len(S)-K 
    result=0
    i=0
    while i<=j:
        if S[i]=='-':
            S[i]='+'
            cnt=0
            while(cnt+1<K):
                cnt+=1
                S[i+cnt]=flip(S[i+cnt])
            #print('S:', S)
            result+=1
        i+=1
    
    while i<len(S):
        if S[i]=='-':
            return "IMPOSSIBLE"
        i+=1
                
        
    #SOLVE

#    result = min(S,K)*P*min(J,K)
    
        
    return result

def flip(s):
    if s=='-':
        return '+'
    else:
        return '-'

def main():
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        if case == "Case #29:":
            j=1
        result = solve()
        
        gcj.writefile(case, result)
        print(case, result)

main()
