#!/usr/bin/env python

import sys
from collections import deque

def Solve(A, motes):
        #print A, motes
        while(motes and A > motes[0]):
                A += motes[0]
                motes.popleft()
        if not motes: return 0
        else:
                if (2*A-1 > motes[-1]): return 1
                copy1 = deque(list(motes)[:])
                copy1.appendleft(A-1)
                copy2 = deque(list(motes)[:])
                copy2.pop()
                if A > 1:
                        cnt = min(Solve(A, copy1), Solve(A, copy2))
                else:
                        cnt = Solve(A, copy2)
                return 1+cnt
                

def main():
        infile = open(sys.argv[1], 'r')
        inp = infile.readlines()
        T = int(inp[0])
        strn = 1
        for i in range(T):
                (A, N) = map(int, inp[strn].split())
                motes = map(int, inp[strn+1].split())
                strn += 2
                motesd=deque(sorted(motes))
                print 'Case #'+str(i+1)+': '+str(Solve(A, motesd))



if __name__=='__main__':
        main()
