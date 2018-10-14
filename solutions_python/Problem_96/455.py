fi = open("B-large.in", "r")
fo = open("B-large.out", "w")
test = int(fi.readline())
for t in xrange(test): 
	L = map(int, fi.readline().split())
	n, s, p, k, res = L[0], L[1], L[2], 0, 0
	for i in xrange(3, len(L)):
		if (L[i] >= 2 and L[i] <= 28) and (L[i] == 3 * p - 3 or L[i] == 3 * p - 4): k += 1
		elif L[i] >= 3 * p - 2: res += 1
		
	res += min(s, k)
	fo.write('Case #%d: %d\n' %(t + 1, res))
