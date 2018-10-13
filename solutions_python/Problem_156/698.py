import itertools

possible_timings = {}
for k in xrange(1, 10):
	possible_timings[k] = [(k, 0)]
	best_time = k
	for i in xrange(1, k):
		x = k / (i + 1)
		if (k % (i + 1) <> 0):
			x += 1
		if (x + i) >= best_time:
			pass
		else:
			best_time = x + i
			possible_timings[k].append((x, i))
	
	
inf = open("inb.txt", 'r')
outf = open("outb.txt", 'w')

t = int(inf.readline())
for k in xrange(0, t):
	d =  int(inf.readline())
	p = map(int, inf.readline().split())
	
	possible_individual_timings = []
	for pi in p:
		possible_individual_timings.append(possible_timings[pi])
	#print possible_individual_timings
	scheds = itertools.product(*possible_individual_timings)
	best_time = 10
	#print("Case #" + str(k + 1) + ": ")
	for s in scheds:
		#print s
		tt1 = 0
		tt2 = 0
		for (t1, t2) in s:
			tt1 = max(tt1, t1)
			tt2 = tt2 + t2
		if (tt1 +tt2 < best_time):
			#print tt1, tt2
			best_time = tt1 + tt2
	outf.write("Case #" + str(k + 1) + ": ")	
	outf.write(str(best_time) + "\n")
outf.close()
			
		
		
		
