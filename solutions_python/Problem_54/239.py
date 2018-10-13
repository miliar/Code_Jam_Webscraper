

def gcd(a, b):
	while b != 0:
		t = b
		b = a%b
		a = t
	return a

T = input()
for t in range(1, T+1):
	tmp = raw_input().split()
	N = int(tmp[0])
	V = []
	for w in tmp[1:]:
		V.append(int(w))
	

	difs = []
	for i in range(N):
		for j in range(N):
			if i == j or V[i] <= V[j]:
				continue;
			dif = V[i]-V[j]
			difs.append(dif);
			
	
	K = difs[0]
	for i in range(1, len(difs)):
		K = gcd(K, difs[i])
		
	
	oldvalue = -1
	for w in V:
		value = w%K
		
		value = (K - w%K)%K
		if oldvalue != -1 and oldvalue != value:
			oldvalue = 0
			break;
		oldvalue = value
	
	print "Case #" + str(t) + ": " + str(oldvalue)