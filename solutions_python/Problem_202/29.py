import Queue
from collections import defaultdict

def match(g):
	matches = {}
	visited = {node:False for node in g}


	def visit(node):
		if visited[node]:
			return False
		visited[node] = True
		for nextnode in g[node]:
			if nextnode not in matches or visit(matches[nextnode]):
				matches[node] = nextnode
				matches[nextnode] = node
				return True
		return False

	found = True
	while found:
		found = False
		visited = {node:False for node in g}
		for node in g:
			if node not in matches and not visited[node] and node[1] == 0:
				found = found or visit(node)

	return matches


def buildgraph(N, plusset):
	diag0 = set(range(-N+1, N))
	diag1 = set(range(0, 2*N-1))

	invaliddiag0 = set([(i-j) for i,j in plusset])
	invaliddiag1 = set([(i+j) for i,j in plusset])

	diag0 = diag0 - invaliddiag0
	diag1 = diag1 - invaliddiag1

	g = defaultdict(list)

	for i in range(N):
		for j in range(N):
			diag0id, diag1id = i-j, i+j
			if diag0id in diag0 and diag1id in diag1:
				g[(diag0id,0)].append((diag1id,1))
				g[(diag1id,1)].append((diag0id,0))

	return g

def process(N, plusset, crossset):
	oldmodles = {node:'+' for node in plusset}
	oldmodles.update({node:'x' for node in crossset})
	oldmodles.update({node:'o' for node in set(plusset) & set(crossset)})

	g = buildgraph(N, plusset)
	matches = match(g)

	for (k,d), (k2,d2) in matches.iteritems():
		if d==0:
			plusset.append(((k2+k)/2,(k2-k)/2))

	rows = list(set(range(N)) - set([i for i, j in crossset]))
	columns = list(set(range(N)) - set([j for i, j in crossset]))

	assert(len(rows) == len(columns))
	crossset.extend(zip(rows,columns))

	newmodels = {node:'+' for node in plusset}
	newmodels.update({node:'x' for node in crossset})
	newmodels.update({node:'o' for node in set(plusset) & set(crossset)})

	update = {}

	for node, value in newmodels.iteritems():
		if node not in oldmodles or value != oldmodles[node]:
			update[node] = value

	return len(crossset) + len(plusset), update

def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		N, M = map(int, raw_input().strip().split())
		crossset, plusset = [], []

		for _ in range(M):
			c, i, j = raw_input().strip().split()
			i, j = int(i)-1, int(j)-1
			if c == '+' or c == 'o':
				plusset.append((i,j))
			if c == 'x' or c == 'o':
				crossset.append((i,j))

		points, update = process(N, plusset, crossset)
		print 'Case #' + str(caseno+1) + ':', points, len(update)
		for (i,j), value in update.iteritems():
			print value, i+1, j+1

run()