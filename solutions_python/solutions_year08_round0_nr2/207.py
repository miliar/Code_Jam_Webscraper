import sys

def convtime(s, T):
	[h,m] = s.split(':')
	return 10*(int(h) * 60 + int(m) + T)

def trainsort(x,y):
	if x[0] > y[0]:
		return 1
	if x[0] == y[0]:
		return 0
	return -1


N = int(sys.stdin.readline())
for number in xrange(N):
	T = int(sys.stdin.readline())
	l = sys.stdin.readline().split(' ')
	NA = int(l[0])
	NB = int(l[1])
	depart = [[], []]
	arrive = [[], []]

	for i in xrange(NA):
		l = sys.stdin.readline().split(' ')
		dep = l[0]
		arr = l[1]
		depart[0].append ([convtime(dep,0)+1, '-'])
		arrive[1].append ([convtime(arr,T), '+'])
	for i in xrange(NB):
		l = sys.stdin.readline().split(' ')
		dep = l[0]
		arr = l[1]
		depart[1].append ([convtime(dep,0)+1, '-'])
		arrive[0].append ([convtime(arr,T), '+'])

	A = depart[0] + arrive[0]
	B = depart[1] + arrive[1]
	A.sort (trainsort)
	B.sort (trainsort)

	tot = 0
	minA = 0
	minB = 0
	for i in A:
		if i[1] == '+':
			tot += 1
		else:
			tot -= 1
			if tot < minA:
				minA = tot

	tot = 0
	for i in B:
		if i[1] == '+':
			tot += 1
		else:
			tot -= 1
			if tot < minB:
				minB = tot

	print "Case #%d: %d %d" % (number+1, -minA, -minB) 
					



