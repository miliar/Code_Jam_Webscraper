import sys

def gcd(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a

fin = sys.stdin

C = int (fin.readline())

for c in xrange(C):
    n = map(int, fin.readline().split())
    N = n[0]
    n = n[1:]
    
    diffs = []
    
    for a in xrange(N):
	for b in xrange(a):
	    diffs.append(abs(n[a] - n[b]))
	    

    T = diffs[0]
    for t in diffs:
	T = gcd(T, t)

    if n[0] % T == 0:
	y = 0
    else:
	y = T - (n[0] % T)
    
    print "Case #" + str(c+1) + ": " + str(y)