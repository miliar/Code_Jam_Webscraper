from math import sqrt, pow, log, ceil, log10, floor
from sys import stdin, setrecursionlimit
import copy
import random

setrecursionlimit(100000)
debug = 0

dic = {}

def GetN(eatList):

    n = 0

    for i in eatList:
        n = n * 10
        n = n + i

    return n

def algsolve(triv, eatList):

    if debug:
        print "testing with", eatList

    a = max(eatList)

    if a <= 3:
        return a

    eatList.sort()

    n = GetN(eatList)

    if n in dic:
        return dic[n]

    sollog = a

    for i in range(1, a):
        newlist = copy.deepcopy(eatList)

        newlist.remove(a)
        newlist.append(i)
        newlist.append(a - i)

        sollog = min(sollog, 1 + algsolve(triv, newlist))

    rep = sollog
    
    if debug:
        print "rep for ", eatList, rep

    dic[n] = rep

    return rep


def solve(eatList):

    triv = max(eatList)
    smart = algsolve(triv, eatList)

    rep = min(triv, smart)

    return rep

T = int(stdin.readline())

for i in range(1,T+1):
    
    D, = map(int, stdin.readline().split(' '))
    eatList = map(int, stdin.readline().split(' '))

    print "Case #" + str(i) + ":", 

    if debug:
        print
        print D, " then ", eatList

    eatList.sort()
    rep = solve(eatList)

    if rep > max(eatList):
        print "prb"
        exit(-1)

    print rep
