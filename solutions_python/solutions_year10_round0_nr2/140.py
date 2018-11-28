
def gcd(a,b):
	while(a and b):
		if a>b:
			a = a % b
		else:
			b = b % a
	if a>b:
		return a
	return b

Z = int(raw_input())

for z in range(0,Z):
	S = raw_input().split()
	T = [int(x) for x in S]
	N = T[0]
	T[0] = 0
	g = 0

	for i in range(1, N):
		g = gcd(g, abs(T[i]-T[i+1]))

	print "Case #" + str(z+1) + ": " + str((g - (T[1] % g)) % g)

