f = open("a.in")
d = f.read()
f.close()

d = d.split("\n")

t = int(d[0])

f = open("a.out", "w")
TI = 1
for ti in xrange(t):
	l = d[TI].split(" ")
	l = [int(e) for e in l]
	X, S, R, T, N = l[0], float(l[1]), float(l[2]), float(l[3]), l[4]
	TI += 1
	walks = []
	LEN = 0
	for j in xrange(N):
		lll = d[TI].split(" ")
		B, E, w =float(lll[0]), float(lll[1]), float(lll[2])
		walks += [(w, E - B)]
		LEN += E - B
		TI += 1
		
	queda = X - LEN
	walks += [(0.0, queda)]
	
	walks.sort()
	#walks.reverse()
	USED = 0
	
	SOL = 0.0
	
	for walk in walks:
		#print walk
		if True:#USED <= T:
			vel = walk[0] + R
			#print vel,
			time = walk[1] / vel
			#print time
			if (time < T - USED):
				SOL += time
				#print "AA"
			else:
				if (T - USED) > 0:
					SOL += (T - USED)
					queda_tiempo = (time - (T - USED))
					pude_haber_recorrer = queda_tiempo * (walk[0] + R)
					#print T - USED, queda_tiempo, pude_haber_recorrer
					SOL += pude_haber_recorrer / (walk[0] + S)
					#print "BB"
				else:
					SOL += walk[1] / (walk[0] + S)
					#print "CC"
				time = T - USED
				
			USED += time
			#print "A", USED, time
	
	#print X, S, R, T, N
	S = "Case #%d: %.8f" % ((ti+1), SOL)
	print S
	f.write("%s\n" % S)
f.close()

