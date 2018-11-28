#!/usr/bin/python3
from operator import itemgetter, attrgetter
import math
import sys

def readline():
    return sys.stdin.readline().strip()

def read():
    global N,C,M,P,B
    a=readline().split()
    N,C,M=[int(x) for x in a]
    P=list()
    B=list()
    for i in range(M):
        a=[int(x) for x in readline().split()]
        P.append(a[0])
        B.append(a[1])

def solve():
    read()
    man=[0]*(C)
    seat=[0]*(N)
    for i in P:
        seat[i-1]+=1
    for i in B:
        man[i-1]+=1
    man_max=max(man)
#    print(seat,man,man_max)
    ans=man_max
    while True:
        room=0
        over=0
        for i in range(N):
            if seat[i]>ans:
 #               print(i,room,over)
                over+=seat[i]-ans
                if room >= over:
                    pass
                else:
                    ans+=1
                    break
            else:
                room+=ans-seat[i]
        else:
            break
#    ansstr="{0} {1}".format(ans,over)
#    print(ansstr)
    printans("{0} {1}".format(ans,over))



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
