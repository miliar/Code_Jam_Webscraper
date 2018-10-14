import sys

N = int(sys.stdin.readline())
for number in xrange(N):
	engines = dict()
	S = int(sys.stdin.readline())
	for i in xrange(S):
		name = sys.stdin.readline()	
		engines[name] = []
	Q = int(sys.stdin.readline())
	for i in xrange(Q):
		name = sys.stdin.readline()	
		engines[name].extend ([i])
	
	# Algorithm: Pick the longest possible time
	done = False
	time = 0
	switches = 0
	current = ""
	while not done:
		mx = 0
		for n in engines:
			if n == current:
				continue

			if len(engines[n]) == 0:
				done = True
				break
			if engines[n][0] >= mx:
				mx = engines[n][0]
				cand = n
		if done == True:
			break
		time = mx
		current = cand
		#print "Switched to %s at time %d" % (current[:-1], time)
		for n in engines:
			while len(engines[n]) > 0 and engines[n][0] < time:
				engines[n].remove (engines[n][0])

		if time > 0:
			switches = switches + 1

	print "Case #%d: %d" % (number+1, switches) 
					



