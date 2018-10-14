def gcd(n1, n2):
	if (n2 > 0):
		return gcd(n2, n1%n2)
	else:
		return n1

def dAll(M, a):
	for i in a:
		if i%M != 0:
			return 0
	return 1



T = int(input())
for t in range(T):
	linha = raw_input()
	a = linha.split(" ")
	a[0] = -1
	for i in range(len(a)):
		a[i] = int(a[i])
	a.sort()
	a[0] = a[1]
	
	n = 0
	for i in range(1, len(a)):
		if a[n] != a[i]:
			n = n+1
			a[n] = a[i]

	n = n+1
	M = a[1]-a[0]
	for i in range(n):
		for j in range(i+1, n):
			M = gcd(M, a[j]-a[i])
	
	if dAll(M, a):
		print "Case #%d: %d" % (t+1, 0)
		#print "Case #" t+1 ": " 0
	else:
		print "Case #%d: %d" % (t+1, M-(a[0]%M))
		#print "Case #", t+1, ": ", M-(a[0]%M)
