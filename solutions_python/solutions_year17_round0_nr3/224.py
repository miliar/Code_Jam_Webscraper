from decimal import *
from math import log10
from collections import deque

in_file = open('C-large.in', 'r')
out_file = open('finish.in', 'w')
temp = {}
getcontext().prec = 20


##k = Decimal(allsuc * (left + back + 1) + (1 - allsuc) * ((left + back + 1) + arr1[1] + 1))

def solve(bathnum, human):
    k = bathnum
    d = dict()
    d[bathnum] = 1
    ls = None
    rs = None
    sum = 0
    while human > sum:
        p = max(list(d.keys()))
        m = p - 1
        a = m // 2
        b = m - a
        ls = a
        rs = b
        if a > 0:
            if a not in d:
                d[a] = d[p]
            else:
                d[a] += d[p]
        if b > 0:
            if b not in d:
                d[b] = d[p]
            else:
                d[b] += d[p]
        sum += d[p]
        if sum >= human:
            break
        d.pop(p, None)
    return str(max(ls, rs)) + ' ' + str(min(ls, rs))


p = []
for line in in_file:
    p.append(line)
n = p[0]
q = 1
i = 1
answer = None
ques = []
getcontext().prec = 20
while q < len(p):
    m = p[q].strip().split()
    answer = solve(int(m[0]), int(m[1]))
    print("Case #%d: " % (i) + str(answer))
    i += 1
    q += 1