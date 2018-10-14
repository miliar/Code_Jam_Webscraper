import sys, math
debug = sys.stdout

sys.stdin  = open('A-large.in')
sys.stdout = open('A.out', 'w')

# Input

# The first line of the input gives the number of test cases, T. T test cases follow, each specifies a class diagram. The first line of each test case gives the number of classes in this diagram, N. The classes are numbered from 1 to N. N lines follow. The ith line starts with a non-negative integer Mi indicating the number of classes that class i inherits from. This is followed by Mi distinct positive integers each from 1 to N representing those classes. You may assume that:

# If there is an inheritance path from X to Y then there is no inheritance path from Y to X.
# A class will never inherit from itself.
# Output

#For each diagram, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is "Yes" if the class diagram contains a diamond inheritance, "No" otherwise.
sys.setrecursionlimit(2000);
class Class(object):
	def __init__(self, id):
		self.id = id
		self.parents = []
		self.visitedBy = set()

	def __repr__(self):
		return "Class(%d : %s : %s)" %(self.id, [p.id for p in self.parents], [v.id for v in self.visitedBy])

def walk(walker, cls):
	if walker in cls.visitedBy:
		return True
	cls.visitedBy.add(walker)

	return any(walk(walker, c) for c in cls.parents)

def solve(classes):
	for cls in classes:
		for parent in cls.parents:
			if walk(cls, parent):
				return "Yes"

	return "No"

for i in xrange(input()):
	n = int(raw_input())
	classes = [Class(c + 1) for c in xrange(n)]

	for cls in classes:
		parentIds = map(int, raw_input().split(' ')[1:])
		cls.parents = [classes[p - 1] for p in parentIds]

	print 'Case #%d: %s' % (i+1, solve(classes))