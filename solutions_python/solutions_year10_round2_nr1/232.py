import sys

class Tree:
	def __init__(self):
		self.dirs = {}

	def add_path(self, path):
		if not path: return 0
		if path[0] not in self.dirs:
			self.dirs[path[0]] = Tree()
			return 1 + self.dirs[path[0]].add_path(path[1:])
		else:
			return self.dirs[path[0]].add_path(path[1:])

if __name__=="__main__":
	f = open(sys.argv[1])
	cases = int(f.readline())
	for case in xrange(1, cases+1):
		paths = Tree()
		oldpaths, newpaths = map(int, f.readline().split())
		for p in xrange(oldpaths):
			path = f.readline().strip()
			parts = path[1:].split("/")
			paths.add_path(parts)
		total = 0
		for p in xrange(newpaths):
			path = f.readline().strip()
			parts = path[1:].split("/")
			total += paths.add_path(parts)
		print "Case #%d: %d" % (case, total)
