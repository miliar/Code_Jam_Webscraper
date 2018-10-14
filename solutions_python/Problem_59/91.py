t = int(raw_input())

class Trie:
	def __init__(self):
		self.d = {}
	def add(self,s):
		if len(s) == 0:
			return
		if s[0] in self.d:
			self.d[s[0]].add(s[1:])
		else:
			a = Trie()
			a.add(s[1:])
			self.d[s[0]] = a
	def size(self):
		size = 1
		for x in self.d.itervalues():
			size+=x.size()
		return size

def diff(a,b):
	size = 0
	for x in a.d:
		if x in b.d:
			size += diff(a.d[x], b.d[x])
		else:
			size += a.d[x].size()
	return size

for i in xrange(t):
	n, m = map(int,raw_input().split())
	a = Trie()
	for j in xrange(n):
		a.add(raw_input().split("/")[1:])
	b = Trie()
	for j in xrange(m):
		b.add(raw_input().split("/")[1:])
	print "Case #%d: %d" % (i+1,diff(b,a))
