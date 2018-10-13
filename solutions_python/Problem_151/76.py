import sys


def f(level):
	if level == em:
		for s in stacks:
			if len(s) == 0:
				return;
		c = 0
		for s in stacks:
			tree = []
			for st in s:
				for i in range(len(st) + 1):
					tree += [ st[:i] ]
			c += len(set(tree))
			#print set(tree)
		if c > maxa[0]:
			maxa[0] = c
			maxb[0] = 1
		elif c == maxa[0]:
			maxb[0] += 1
	else:
		for i in range(len(stacks)):
			stacks[i] += [ nodes[level] ]
			f(level+1)
			del stacks[i][-1]


ecase = int(sys.stdin.readline().strip())
for ecount in range(1, ecase+1):
	tu = sys.stdin.readline().strip().split()
	em, en = int(tu[0]), int(tu[1])
	nodes = range(em);
	for i in range(len(nodes)):
		nodes[i] = sys.stdin.readline().strip()
	stacks = [ [] for x in range(en) ]
	maxa = [0]
	maxb = [0]
	f(0)
	print "Case #%d: %d %d" % (ecount, maxa[0], maxb[0])

