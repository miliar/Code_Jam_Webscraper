import inspect
base = inspect.getfile(inspect.currentframe())[:-3]
data = file(base+'.in', 'r')
out = file(base+'.out', 'wb')

import collections
T = int(data.readline())
for case in range(1,T+1):
	v = data.readline().split()
	pair = lambda a,b: tuple(sorted([a, b]))
	n = lambda: v.pop(0)
	C = int(n())
	combine = {}
	for i in range(C):
		a,b,c = n()
		combine[pair(a, b)] = c
	D = int(n())
	oppose = collections.defaultdict(list)
	for i in range(D):
		a,b = n()
		oppose[a].append(b)
		oppose[b].append(a)
	N = int(n())
	elemseq = list(*v)
	print combine, dict(oppose), elemseq
	result = []
	for elem in elemseq:
		result.append(elem)
		if len(result) >= 2:
			lpair = pair(result[-1], result[-2])
			if lpair in combine:
				result[-2:] = [combine[lpair]]
		if len(result) >= 2:
			seeking = oppose[result[-1]]
			for relem in result[:-1]:
				if relem in seeking:
					result = []
					break
	print result
	out.write("Case #{0}: [{1}]\n".format(case, ", ".join(result)))
