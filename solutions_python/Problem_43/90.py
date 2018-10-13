

T = int(raw_input())

for Cs in xrange(1,T+1):
	L = raw_input().strip()
	
#	print L
	Ls = set(L)
	
	base = len(Ls)
	if base == 1: base = 2
	dig = {}
	
	dig[L[0]] = 1
	curdig = 1
	for i in L[1:]:
		if i not in dig:
			if curdig == 1:
				dig[i] = 0
			else:
				dig[i] = curdig
			curdig += 1
	
	op = ""
	for i in L:
		if dig[i] < 10:
			op += chr(48 + dig[i])
		else:
			op += chr(65 - 10 + dig[i])
	
	print "Case #%d: %d" % (Cs, int(op,base))
	