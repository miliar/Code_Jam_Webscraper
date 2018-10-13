class Dir():
	def __init__(self):
		self.subs = {}
		
	def add(self, subpath):
		if not subpath:
			return 0
		parts = subpath.split('/', 1)
		folder = parts[0]
		if len(parts) > 1:
			next = parts[1]
		else:
			next = None
		
		if folder in self.subs:
			return self.subs[folder].add(next)
		else:
			self.subs[folder] = Dir()
			return 1 + self.subs[folder].add(next)
		
def solve(tc):
	n, m = map(int, raw_input().split())
	base = Dir()
	for i in xrange(n):
		base.add(raw_input()[1:])
	
	ans = 0
	for j in xrange(m):
		ans += base.add(raw_input()[1:])
	
	print "Case #%d: %d"%(tc, ans)
	
for tc in xrange(input()):
	solve(tc+1)
