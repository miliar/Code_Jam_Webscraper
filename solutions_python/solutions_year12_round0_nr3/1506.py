
def recurse(n,m):
	if n == m:
		return 0
	for x in range(1,len(n)):
		if n[-x:]+n[:-x] == m:
			return 1
	else:
		return 0

with file('C-small-attempt1.in.txt') as f:
	solution = open('solution.txt','w')
	t = int(f.readline().strip())
	for i in range(0,t):
		line = [x for x in f.readline().strip().split(' ')]
		count = []
		for n in range(int(line[0]), int(line[1])+1):
			n = str(n)
			for m in range(int(n),int(line[1])+1):
				m = str(m)
				if len(n) != len(m):
					continue
				if recurse(n,m) == 1:
					if set([n,m]) not in count:
						count.append(set([n,m]))
		solution.write("Case #%i: %i\n"%(i+1, len(count)))
print 'done'