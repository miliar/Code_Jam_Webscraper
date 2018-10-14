cases = int(raw_input())

debug = False

for case in range(cases):

	N,K = [int(i) for i in raw_input().split()]

	if debug:
		print "N = %s" % str(N)
		print "K = %s" % str(K)

	parts = [N]

	partSet = {}
	partSet[N] = 1

	while K > 0:

		#print parts

		l = max(parts)
		#print l

		# optimalization for small 2
		if l == 1 or l == 0:
			maxLR = 0
			minLR = 0
			break

		multiplier = partSet[l]

		if l % 2 == 0:
			a = (l/2)-1
			b = l/2
		else:
			a = l/2
			b = l/2


		

		K -= multiplier

		if a in partSet:
			partSet[a] += multiplier
		else:
			partSet[a] = multiplier

		if b in partSet:
			partSet[b] += multiplier
		else:
			partSet[b] = multiplier

		
		if a not in parts:
			parts.append(a)
		if b not in parts:
			parts.append(b)

		parts.remove(l)
		partSet[l] = 0

	maxLR = l/2
	minLR = maxLR

	if l % 2 == 0:
		minLR = minLR - 1
	
	if debug:
		print "minLR: " + str(minLR)
		print "maxLR: " + str(maxLR)



	print "Case #" + str(case+1) + ": " + str(maxLR) + " " + str(minLR)