# text messaging outrage
for case in range(input()):
	P, K, L = map(int, raw_input().split())
	freq = map(int, raw_input().split())
		
	freq.sort()
	freq.reverse()
	
	bins = []
	
	for k in range(K):
		bins.append(list())
	
	pos = 0
	total = 0
	impossible = False
	for f in freq:
		bins[pos].append(f)
		bin_size = len(bins[pos])
		if bin_size > P:
			impossible = True
			break
		total += len(bins[pos])*f
		pos += 1
		if pos >= K:
			pos = 0
		
	if impossible:
		result = "Impossible"
	else:
		result = str(total)

	print 'Case #%s: %s' % (case + 1, result)
