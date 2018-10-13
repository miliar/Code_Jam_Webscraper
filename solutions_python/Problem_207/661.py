import sys
import random

sys.setrecursionlimit(2000)

dr = [2,2,0,0,0,2]
dy = [0,2,2,2,0,0]
db = [0,0,0,2,2,2]

def allow(a, b):
    if all(x in [0,1,5] for x in [a, b]):
        return False
    if all(x in [1,2,3] for x in [a, b]):
        return False
    if all(x in [3,4,5] for x in [a, b]):
        return False
    return True

class Again(Exception):
    pass

count = 0

def toplevel(colors):
    r,o,y,g,b,v = colors
    if (r + o + v >= g + b + y + 1 or 
        y + o + g >= r + v + b + 1 or
        b + v + g >= r + y + o + 1):
        return False
    return True

def find(last, cur, colors):
    global count
    count += 1
    if count > 6000:
        raise Again
    #print cur, "RYB", [rr,ry,rb], "ROYGBV", colors
    r,o,y,g,b,v = colors
    if sum(colors) == 0:
        if not allow(cur[0], cur[-1]):
            return None
        return cur
    if (r + o + v > g + b + y + 1 or 
        y + o + g > r + v + b + 1 or
        b + v + g > r + y + o + 1):
        return None
    y = range(6)
    random.shuffle(y)
    for i in y:
        if colors[i] > 0 and allow(last, i):
            nc = colors[:]
            nc[i] -= 1
            x = find(i, cur+[i], nc)
            if x is not None:
                return x
    return None

M = "ROYGBV"

def read(x):
    if x is None:
        return "IMPOSSIBLE"
    else:
        return "".join(M[i] for i in x)

for tc in xrange(input()):
    colors = map(int, raw_input().split())
    rem = colors[0]
    while True:
        try:
            count = 0
            if not toplevel(colors[1:]):
                x = None
                break
            x = find(-1, [], colors[1:])
            break
        except Again:
            continue
    print "Case #%d: %s" % (1+tc, read(x))
