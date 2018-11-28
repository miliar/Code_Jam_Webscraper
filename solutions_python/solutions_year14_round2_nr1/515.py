import sys
from collections import Counter
sys.stdin = open("A-small-attempt0.in", "r")
def solve():
    n = int(input())

    str1 = list(sys.stdin.readline().strip())
    p1 = []
    p1c = []
    l = "@"
    cnt = 0
    for c in str1:
        if c==l:
            cnt += 1
        else:
            if l != "@":
                p1.append(l)
                p1c.append(cnt)
            cnt = 1
            l = c
    p1.append(l)
    p1c.append(cnt)

    str2 = list(sys.stdin.readline().strip())
    p2 = []
    p2c = []
    l = "@"
    cnt = 0
    for c in str2:
        if c==l:
            cnt += 1
        else:
            if l != "@":
                p2.append(l)
                p2c.append(cnt)
            cnt = 1
            l = c
    p2.append(l)
    p2c.append(cnt)

    if p1==p2:
        res = 0
        for i in xrange(len(p1c)):
            res += abs(p1c[i]-p2c[i])
        return str(res)
    else:
        return "Fegla Won"

    print p1
    print p1c
    print p2
    print p2c
    return "aga"
T = int(input())
for _t in xrange(T):
    print "Case #" +str(_t+1) + ": " + solve()