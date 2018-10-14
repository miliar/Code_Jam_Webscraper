#!/usr/bin/python2

def readf(f):
    rline = lambda : [int(v) for v in f.readline().split(' ')]
    n, m = rline()
    lawn = []
    for i in range(n):
        lawn.append(rline())
    return lawn

def lower_max(lawn):
    for line in lawn:
        for c in line:
            if c > 100:
                return False
    return True
    
def test(lawn):
    if not lower_max(lawn):
        return False
    n, m = len(lawn), len(lawn[0])
    if n == 1 or m == 1:
        return True
    for r in range(n):
        for c in range(m):
            h = lawn[r][c]
            hasHigher = False
            for sr in range(n):
                if lawn[sr][c] > h:
                    hasHigher = True
                    break
            for sc in range(m):
                if lawn[r][sc] > h and hasHigher:
                    return False
    return True
            
    
if __name__=="__main__":
    f = file("lawn.case");
    t = int(f.readline())
    for i in range(t):
        print "Case #%d:" % (i + 1), "YES" if test(readf(f)) else "NO"

    
