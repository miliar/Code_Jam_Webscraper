
def gcd(a,b):
	while min(a,b) > 0:
		if a < b:
			b = b % a
		else:
			a = a % b
	return max(a,b)

C = input()

for c in range(C):
	tmp = [int(x) for x in raw_input().split()]
	N = tmp[0]
	t = tmp[1:]
	
	tm = [x-min(t) for x in t]
	
	T = tm[0]
	for x in tm[1:]:
		T = gcd(T,x)
	
	print "Case #%s: %s" % ( c+1, (T-t[0]%T)%T )
