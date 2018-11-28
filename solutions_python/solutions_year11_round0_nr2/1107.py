base = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
T = int(raw_input())
for _ in xrange(T):
	l = raw_input().split()
	#print l
	C = int(l[0])
	out = []
	nbase = []
	opposed = []
	els = ""
	for c in l[1:C+1]:
		nbase.append(((c[0], c[1]), c[2]))	
	#print nbase
	D = int(l[C+1])
	for d in l[C+2:C+D+2]:
		opposed.append((d[0], d[1]))	
	#print opposed
	N = int(l[C+D+2])
	#print N
	if (N > 0):
		els = l[C+D+3]
	#print els
	for e in els:
		#print "see %s" % e
		out.append(e)
		if (len(out) > 1) :
			for n in nbase:
				if ((
					 not (out[-1] == out[-2]) 
					 or
					 (n[0][0] == n[0][1])
					)
					and 
					(out[-1] in n[0]) 
					and 
					(out[-2] in n[0])):
					
					#print "replace %s and %s with %s" % (out[-1], out[-2], n[1])
					out = out[:-2] 
					out.append(n[1])					
		for o in opposed:
			if (o[0] in out and o[1] in out):
				out = []
				#print "opposed %s and %s" % (o[0], o[1])
	
	print "Case #%d: [%s]" % (_+1, ", ".join(out))