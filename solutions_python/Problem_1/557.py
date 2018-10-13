import sys

out = {}

f = open(sys.argv[1])
try:
	for N in range(int(f.next())):
		
		engines = []
		for e in range(int(f.next())):
			engines.append(f.next().strip())
		
		switches = 0
		unused = set(engines)
		for q in range(int(f.next())):
			q = f.next().strip()
			
			if not q in unused:
				continue
			
			unused.remove(q)
			if len(unused) == 0:
				switches += 1
				unused = set(engines)
				unused.remove(q)
		
		out[N + 1] = switches
		
finally:
	f.close()

f = open(sys.argv[2], 'w')
try:
	f.write('\n'.join('Case #%s: %s' % (k, v) for k, v in out.items()))
finally:
	f.close()