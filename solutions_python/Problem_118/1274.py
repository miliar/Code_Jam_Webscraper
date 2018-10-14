import numpy as np, sys, math

def ispal(i):
    l = list(str(i))
    return l == list(reversed(l))

def proc(case):
    a, b = case
    res = 0
    for i in range(int(math.ceil(math.sqrt(a))), 1+int(math.sqrt(b))):
        if ispal(i) and ispal(i*i):
            res += 1

    return res

with open(sys.argv[1]) as f:
    t = int(f.readline())

    for i in range(t):
        case = map(int, f.readline().split())
        print 'Case #%d: %s' % (i+1, proc(case))
