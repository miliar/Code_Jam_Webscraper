from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

def getLeft(j, st):
    k = j - 1
    while (st[k] == 0):
        k -= 1
    return j - k
        
def getRight(j, st):
    k = j + 1
    while (st[k] == 0):
        k += 1
    return k - j

def sol(n, k):

    debug = True

    st = [0] * (n+2)
    st[0] = 1
    st[n+1] = 1

    for i in range(k):
        if debug:
            print "Current before customer ", i, st
        # where to go
        bestMinValue = 0
        bestMaxValue = 0
        bestMinJ = None
        for j, v in enumerate(st):
            if v != 0:
                continue
            left = getLeft(j, st)
            right = getRight(j, st)
            mini = min(left, right)
            maxi = max(left, right)
            # if debug:
            #     print "at", j, "left right min max is", left, right, mini, maxi    
            if mini > bestMinValue:
                bestMinValue = mini
                bestMinJ = j
                bestMax = maxi
            elif mini == bestMinValue and maxi > bestMax:
                bestMinValue = mini
                bestMinJ = j
                bestMax = maxi
        st[bestMinJ] = i + 2

    if debug:
        print "End", st

    j = bestMinJ
    left = getLeft(j, st)
    right = getRight(j, st)
    mini = min(left, right)
    maxi = max(left, right)

    return str(maxi - 1) + ' ' + str(mini - 1)

def fastsol(n, k):

    st = {}
    st[n] = 1
    lg = 1
    i = 0

    while i < k:
        x = max(st)
        l = (x - 1) / 2
        r = x - 1 - l
        stx = st[x]
        del st[x]

        if l in st:
            st[l] += stx
        else:
            st[l] = stx

        if r in st:
            st[r] += stx
        else:
            st[r] = stx

        # if i == 2*lg:
        #     print "DEBUG", i, l, r, st
        #     lg *= 2
        # print "DEBUG", i, l, r, st

        i += stx

    maxi = max(l, r)
    mini = min(l, r)
    return str(maxi) + ' ' + str(mini)

T = int(stdin.readline())

for i in range(1,T+1):

    n, k = map(int, stdin.readline().split())
    
    print "Case #" + str(i) + ":", 
    print fastsol(n, k)
    
