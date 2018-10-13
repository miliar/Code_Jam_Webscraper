import string


def get_answer(n,s,p,scores):
	#print "n", n, "s", s, "p", p
	scores.sort(reverse = True)
	#print "sort", scores
	p3 = p*3-3
	nots = 0
	iss = 0
	for par in xrange(n):
		if scores[par]>p3:
			continue
		nots = par
		#print "nots", nots, "par", par, 'score', scores[par]
		iss = 0
		for par2 in xrange(par, n):
			if scores[par2] > max((p3 - 2), 0 ):
				iss=iss+1
				
				if iss >= s:
					#print par2, scores[par2]
					break
				continue
			break
		break
	
	else:
		nots = n
	
	return nots+min(iss,s)
	
	
	
f=open('B-large.in','r')
tcase=int(f.readline())
for times in xrange(tcase):
	try:
		line = f.readline()
	except:
		pass
	scores = string.split(line)
	n = int(scores[0])
	s = int(scores[1])
	p = int(scores[2])
	scores = scores[3:]
	for x in xrange(len(scores)):
		scores[x] = int(scores[x])
	
	ans = get_answer(n,s,p,scores)
	print 'Case #'+str(times+1)+': '+str(ans)


	
	
	