import sys

def ok(n):
    n = str(n)
    for i in xrange(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

lines = sys.stdin.readlines()
n = int(lines[0])
assert len(lines) == n+1
for i in xrange(n):
    m = int(lines[i+1])
    last = 0
    for j in xrange(m+1):
        if ok(j):
            last = j
    print "Case #%d: %d" % (i+1, last)
    
