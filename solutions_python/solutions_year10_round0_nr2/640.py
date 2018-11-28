import math

def PGCD(L):
    def _pgcd(a,b):
        while b: a, b = b, a%b
        return a
    if (len(L) == 1) : return L[0]
    if (len(L) == 2) : return _pgcd(L[0],L[1])
    p = _pgcd(L[0], L[1])
    for x in L[2:]:
        p = _pgcd(p, x)
    return p
    
    

C = int(raw_input())

for i in range(C):
	# Get input
	T = raw_input().split()
	T.pop(0)
	for e in range(len(T)): T[e] = int(T[e])
	
	# Sort data 
	T.sort()
	less = T.pop(0)
	for e in range(len(T)): T[e] -=  less
	
	# Get PGCD 
	P = PGCD(T)
	N = less / P
	
	
	# 
	R = int(math.fabs((less - (N*P)) - P))
	if (less % P == 0): R = 0
	print("Case #"+str(i+1)+": "+str(R))
	
