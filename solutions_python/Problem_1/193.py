
n = int(raw_input())

for case in xrange(1,n+1):
	
	s = int(raw_input())
	
	engines = set()
	
	for i in xrange(s):
		engines.add(raw_input())
	
	q = int(raw_input())
	switches = dict((i,0) for i in engines)
	
	for i in xrange(q):
		eng = raw_input()
		
		for j in switches:
			if switches[j] == "X":
				switches[j] = min(switches.values()) + 1
		switches[eng] = "X"
		
		#print switches
	print "Case #%d: %d" % (case, min(switches.values()))