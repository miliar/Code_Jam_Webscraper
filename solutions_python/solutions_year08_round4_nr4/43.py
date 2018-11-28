#!/usr/bin/env python
import gmpy,math
import sys

f=sys.stdin
n=int(f.next())
def permute(s):
    if len(s) == 1:
        yield s
        return
    for i,j in enumerate(s):
        for k in permute(s[:i]+s[i+1:]):
            yield [j]+k

def evaluate(s,k,p):
    res = []
    for j in range(0,len(s),k):
        piece = s[j:j+k]
        res.extend(piece[y] for y in p)
    c=None
    count = 0
    for j in res:
        if j != c:
            count+=1
            c=j
    return count
    
class Case(object):
    def __init__(self):
        self.res = "Impossible"
        k = int(f.next())
        s = f.next().strip()
        res = []
        for p in permute(range(k)):
            res.append(evaluate(s,k,p))
        self.res = min(res)

    def run(self):
        pass

    def __str__(self):
        return str(self.res)

for case in range(1, n+1):
    c=Case()
    c.run()

    print "Case #%s: %s"%(case,c)


