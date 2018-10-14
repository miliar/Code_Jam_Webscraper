import sys

lines = sys.stdin.readlines()
def parseCase(lines):
    r,t= map(int,lines[0].split(" "))
    return 1, (r,t)

def getCases(lines):
    i =0
    while i < len(lines):
        lines_used, case = parseCase(lines[i:])
        i += lines_used
        yield case

cNum =0

def check(case, answer):
    return True

import math
for c in getCases(lines[1:]):
    cNum +=1
    r,t = c
    t = float(t)
    answer = 0
    a = 0
    b = 10**18
    m = 0
    while True:
        if a == b or a +1 == b: break
        m = (a+b)/2
        n = (2 * m * r - m + 2 * m**2)
        if t > n:
            a = int(m)
        elif t < n:
            b = int(m)
        else:
            break
    answer = m
    if (2 * m * r - m + 2 * m**2) > t:
        answer = m-1
    
    print "Case #%d: %s" % (cNum,str(answer))
