#!/usr/bin/python3
from operator import itemgetter, attrgetter
import math
import sys

def readline():
    return sys.stdin.readline().strip()

def read():
    global N,P,G
    a=readline().split()
    N,P=[int(x) for x in a]
    a=readline().split()
    G=[int(x) for x in a]

def solve():
    read()
    ans=0
    ama=[0]*P
    for i in G:
        ama[i%P]+=1
    if P==2:
        ans=ama[0]+(ama[1]+1)//2
    elif P==3:
        ans=ama[0]
        add=min(ama[1],ama[2])
        ama[1]-=add
        ama[2]-=add
        ans+=add
        ans+=(ama[1]+2)//3
        ans+=(ama[2]+2)//3
        pass
    printans(ans)

def printans(ans):
    print ("Case #{0}: {1}".format(CASE,ans))

def printmultians(ans):
    print ("Case #{0}:".format(CASE))
    for j in ans:
        print (''.join(j))

def main():
    T=int(sys.stdin.readline())
    global CASE
    for CASE in range(1,T+1):
        ans = solve()

main()
