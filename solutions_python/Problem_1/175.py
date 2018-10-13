import sys, copy

f = open(sys.argv[1], 'r')
for i in range(int(f.readline())):
	search_engines = []
	for j in range(int(f.readline())):
		search_engines.append(f.readline().strip())

	result = 0
	buf = copy.copy(search_engines)
	current = None
	for j in range(int(f.readline())):
		q = f.readline().strip()
		if current!=q:
			#print (buf, q, result)
			try:
				buf.remove(q)
			except:
				pass
			current = q
		if not buf:
			result = result + 1
			buf = copy.copy(search_engines)
			buf.remove(q)

	print 'Case #%d: %d'%(i+1, result)