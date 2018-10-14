import sys

class Tree:
	def __init__(self):
		self.exists = False
		self.children = {}

	def insert(self, path, exists):
		if exists:
			self.exists = True
		if not path:
			return
		spl = path.split('/', 1)
#		print spl
		cur = spl[0]
		if len(spl) > 1:
			rem = spl[1]
		else:
			rem = ''

		if not self.children.has_key(cur):
			self.children[cur] = Tree()
		self.children[cur].insert(rem, exists)

	def tocreate(self):
		ret = 0 if self.exists else 1
#		for child in self.children:
#			print child, self.children[child].tocreate()
		return ret + sum([self.children[child].tocreate() for child in self.children])


def case(P):
	sys.stdout.write('Case #%d: ' % (P+1))
	[n, m] = map(int, sys.stdin.readline().split())
	root = Tree()
	root.exists = True

	for i in xrange(n):
		root.insert(sys.stdin.readline().strip()[1:], True)
	for i in xrange(m):
		root.insert(sys.stdin.readline().strip()[1:], False)
	print root.tocreate()

def main():
	nc = int(sys.stdin.readline())
	for i in xrange(nc):
		case(i)

if __name__ == '__main__':
	main()
