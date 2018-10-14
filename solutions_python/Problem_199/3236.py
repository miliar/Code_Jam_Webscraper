from Queue import PriorityQueue
import sys

T = None
cases = []
with open(sys.argv[1]) as f:
	T = int(f.readline())
	for l in f.readlines():
		o = []
		l = l.split(' ')
		K = int(l[1])
		for p in l[0]:
			if p =='+':
				o.append(1)
			elif p == '-':
				o.append(0)

		cases.append((o,K))

def buildState(s,p):
	# return (len(p)-sum(p),{'s':s,'p':p})
	return (s,{'s':s,'p':p})
def hashState(st):
	return hash(str(st[1]['p']))
def validStates(st,k):
	c = st[1]['p']
	s = st[1]['s']
	vs = []
	for i in range(0,len(c)-(k-1)):
		nc = c[:]
		for j in range(i,i+k):
			nc[j] = 1 - nc[j]
		vs.append(buildState(s+1,nc))
	return vs


for I,C in enumerate(cases):
	K = C[1]
	I = I + 1
	initState = buildState(0,C[0])

	# special case
	if sum(C[0]) == 0:
		if sum(C[0]) % K != 0:
			print "Case #{}: IMPOSSIBLE".format(I)
			continue

	q = PriorityQueue()
	hashes = set()

	q.put(initState)

	solved = False

	while not q.empty():
		state = q.get()

		# victory condition
		if sum(state[1]['p']) == len(state[1]['p']):
			print "Case #{}: {}".format(I,state[1]['s'])
			solved = True
			break

		hashes.add(hashState(state))

		vss = validStates(state,K)
		for vs in vss:
			hsh = hashState(vs)
			if hsh in hashes:
				continue
			q.put(vs)
	if not solved:
		print "Case #{}: IMPOSSIBLE".format(I)




