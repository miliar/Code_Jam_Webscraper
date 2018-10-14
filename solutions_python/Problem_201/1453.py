import math
import sys
sys.setrecursionlimit(100000)
from collections import defaultdict

def dsum(*dicts):
    ret = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            ret[k] += v
    return dict(ret)

    
    
def getDepthAndRemaining(k):
    i = 0
    while k > 0:
        lastI = i
        lastK = k
        k -= 2**i
        i += 1
    return (lastK,lastI)

def getSlots(n,d):
    if d == 0:
        D[(n,d)] = {n:1}
        return {n:1}
    if (n,d) in D:
        return D[(n,d)]
    else:
        l = math.floor((n-1)/2.0)
        r = math.ceil((n-1)/2.0)
        D[(n,d)] = dsum(getSlots(l,d-1),getSlots(r,d-1))
    return D[(n,d)]
 

def getStall(k):
    l = math.floor((k-1)/2.0)
    r = math.ceil((k-1)/2.0)
    return str(int(max(l,r))) + ' ' + str(int(min(l,r)))
 


p1 = open('file','r')
p = p1.read().split('\n')[1:-1]
i = 1
o = open('out.txt','w')


i = 1
D = {}
for l in p:
    [n,k] = map(lambda x: int(x),l.split())
    (r,d) = getDepthAndRemaining(k)
    res = getSlots(n,d)
    keys = sorted(res.keys(),key = lambda x: -x)
    for key in keys:
        r -= res[key]
        if r <= 0:
            o.write('Case #' + str(i) + ': ' + getStall(key) + '\n')
            break
    i += 1
            
p1.close()
o.close()
