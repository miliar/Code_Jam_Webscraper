import sys

def gcd(a,b):
	if a == 0:
		return b
	return abs(gcd(b % a, a))

def work(L):
    if len(L) == 2: return L[1]-L[0]
    d1 = L[1]-L[0]    
    d2 = L[2]-L[1]
    mod = gcd(d1,d2)
    for i in xrange(2,len(L)-1):        
        diff = L[i+1]-L[i]      
        mod = gcd(mod,diff)
    return mod
    
f = sys.stdin
c = int(f.readline())

for case in xrange(1,c+1):
    L = map(int,f.readline().split())
    L =  L[1:]
    S = set(L)
    L = list(S)
    L.sort()
    mod = work(L)
    print "Case #%i: %i"%(case,-L[0]%mod)
    
