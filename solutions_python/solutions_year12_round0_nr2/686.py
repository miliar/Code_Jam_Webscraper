try:
	nTests = int(raw_input())
	
	for test in xrange(1, nTests+1):
		line = raw_input().split()
		N = int(line[0])
		S = int(line[1])
		p = int(line[2])
		googlers = [int(e) for e in line[3:]]
		#print N, S, p, googlers
	
		min_surprising = max(0, 3*p - 4)		# same as p + p-2 + p-2
		min_unsurprising = max(0, 3*p - 2)		# same as p + p-1 + p-1
		count = 0
		n_that_need_surprising = 0;
		#scores_that_need_surprising = []
		#print min_surprising, min_unsurprising
		
		for score in googlers:
			if score >= min_unsurprising:
				count += 1
			else:
				if score < p or score < min_surprising:
					continue
				n_that_need_surprising += 1
				#scores_that_need_surprising.append(score)
		
		#print scores_that_need_surprising
		
		count += min(S, n_that_need_surprising)
		
		print "Case #%d: %d" % (test, count)

except EOFError:
	pass
