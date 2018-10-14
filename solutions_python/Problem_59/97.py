import sys

class Tree:
	def __init__(self):
		self.children = {}
	def add(self, l):
		if len(l) == 0:
			return
		d = l[0]
		r = l[1:]
		if d in self.children.keys():
			self.children[d].add(r)
		else:
			t = Tree()
			t.add(r)
			self.children[d] = t
	
	def walk(self, l):
		if len(l) == 0:
			return 0
		d = l[0]
		r = l[1:]
		if d in self.children.keys():
			return self.children[d].walk(r)
		else:
			t = Tree()
			n = t.walk(r)
			self.children[d] = t
			return n+1



f = sys.argv[1]
fin = open(f)
fout = open(f.replace('in','out'), 'w')
T = int(fin.next())
for k in range(0, T):
	[N, M] = map(int, fin.next().split(' '))
	root = Tree()
	for i in range(0, N):
		root.add(fin.next()[:-1].split('/')[1:])
	print root.children
	total = 0
	for j in range(0, M):
		total += root.walk(fin.next()[:-1].split('/')[1:])
	fout.write("Case #%d: %d\n"%(k+1, total))
