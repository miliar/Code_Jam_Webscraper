
import sys
from math import pi
from decimal import Decimal

name = "B-small"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())



# good for mostly ordered lists
def insertionSort(bots):
   for i in range(1,len(bots)):
     p = i
     c = bots[i]
     while p>0 and bots[p-1]>c:
         bots[p]=bots[p-1]
         p = p-1
     bots[p]=c

def answer(l):
    answer = Decimal(1.0)
    for i in l:
        answer *= (i)
    return answer

def solution(bots,k,pts):
    res = 0
    bots.sort()
    l = len(bots)
    equal = 1

    while pts>0:
        #print(bots)
        while equal < (l) and bots[equal-1]==bots[equal]:
            equal+=1
        #print(equal)
        to_give=pts
        if equal<(l):
            to_give=min(pts,equal*(bots[equal]-bots[equal-1]))
        for i in range(equal):
            bots[i]=min(Decimal(1),bots[i]+to_give/equal)
        pts-=to_give

    #print(bots)
    return answer(bots)

for testCase in range(1, testCases + 1):
    nk = input().split()
    n,k=int(nk[0]),int(nk[1])

    pts=Decimal(input())
    bots = [Decimal(bot) for bot in input().split()]

    res = solution(bots,k,pts)

    print("Case #" + str(testCase) + ": " + ("%.10f" % res))
