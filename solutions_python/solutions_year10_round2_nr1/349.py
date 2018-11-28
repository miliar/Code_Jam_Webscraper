from sys import stdin
ncases = int(stdin.readline())
for x in range(ncases):
	N, M = stdin.readline().strip().split()
	N = int(N)
	M = int(M)
	s = set()
	s.add('/')
	count = 0
	for i in range(N):
		path = stdin.readline().strip()
		s.add(path)
	lastparts = []
	for j in range(M):
		path = stdin.readline().strip()
		parts = path.split('/')[1:]
		for k in range(len(parts)):
			if k >= len(lastparts) or lastparts[k] != parts[k]:
				break
			
		for k in range(1, len(parts) + 1):
			subpath = '/' + '/'.join(parts[:k])
			#print subpath
			if subpath not in s:
				count += 1
				s.add(subpath)
		lastparts = parts
	print 'Case #%d: %d' % (x + 1, count)
		
	
