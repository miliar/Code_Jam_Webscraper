
def getdir(path):
	assert path != '/'
	pos = path.rfind('/')
	return path[:pos]

T = int(raw_input())
for nocase in range(1, T+1):
	result = 0
	exist_path = set([])
	obj_path = set([])
	
	N, M = tuple(map(int, raw_input().split()))
	
	for i in range(N):
		exist_path.add(raw_input())
	for i in range(M):
		obj_path.add(raw_input())
	
	all_existing_dirs = set([])
	for path in exist_path:
		p = path
		while p:
			all_existing_dirs.add(path)
			p = getdir(p)
	
	for path in obj_path:
		p = path
		while p:
			if p not in all_existing_dirs:
				result += 1
				all_existing_dirs.add(p)
			p = getdir(p)
		
	print 'Case #%d: %d' % (nocase, result)
	