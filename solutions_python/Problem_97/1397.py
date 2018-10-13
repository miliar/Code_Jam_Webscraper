import sys

f = map(str.strip, open(sys.argv[1], 'rb').readlines(), "\n")
n = int(f.pop(0))

def solve(a, b):
    c = []
    for i in range(a, b+1):
        c += pairs(i, a, b)
    return set(c)
    
def pairs(d, low, high):
    c = []
    if(d < 10): return c
    b = str(d)
    for i in range(1, len(b)):
        t = b[i:] + b[:i]
        if t[0] == '0' or b == t: continue
        j = int(t)
        if j < low or j > high: continue
        if(j < d): c.append((j, d))
        else: c.append((d, j))
        
    return c

for i in range(n):
    t = f[i].split()
    a = int(t[0])
    b = int(t[1])
    print "Case #%s: %s" % (i+1, len(solve(a, b)))

