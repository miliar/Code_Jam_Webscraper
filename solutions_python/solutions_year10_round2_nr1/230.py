data = open('A-large.in').read().split()
data.reverse()

T = int(data.pop())

for t in range(1, T+1):
	existing, new = int(data.pop()), int(data.pop())
	paths = set()
	def addall(path):
		dirs = path.split('/')[1:]
		for i in range(len(dirs)):
			paths.add(tuple(dirs[0:i+1]))
	
	for i in range(existing):
		addall(data.pop())
	
	size = len(paths)
	
	for i in range(new):
		addall(data.pop())
	
	print "Case #{0}: {1}".format(t, len(paths)-size)