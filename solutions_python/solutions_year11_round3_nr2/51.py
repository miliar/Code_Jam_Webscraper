import sys,copy

a = []
b = []

n = 0
for line in sys.stdin:
	if n == 0:
		n = 1
		continue
	word = line.split()
	L = int(word[0])
	t = int(word[1])
	N = int(word[2])
	C = int(word[3])
	for x in range(C):
		a += [int(word[4+x])]
	ntmp = 0
	npst = 0
	nflg = 0
	nsum = 0
	if L > 0:
		for x in range(N):
			if nflg == 1:
				b += [a[x%C]]
			else:
				npst = ntmp
				ntmp += a[x%C]*2
				if ntmp > t:
					b +=[(a[x%C]  - (t - npst)/2 )]
					nflg = 1
	else:
		for x in range(N):
			b += [a[x%C]]
		
	if nflg == 1:
		nsum = t
	b.sort()
	N = len(b)
	for x in range(N):
		idx = N - 1 - x
		if L > 0:
			L -= 1
			nsum += b[idx]
		else:
			nsum += (b[idx] * 2)
		
	
	print "Case #" + str(n) + ": " + str(nsum)
	a = []
	b = []
	n += 1
