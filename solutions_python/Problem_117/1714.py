Q = input()
M = 0
N = 0
a = []

def extractmin():
	global a
	if len(a) == 0: return 0
	min = a[0][0]
	for i in xrange(0,M):
		for j in xrange(0,N):
			if a[i][j] < min: min = a[i][j]
	return min

def removeCol(i):
	global N
	for x in xrange(0,M):
		del a[x][i]
	N -= 1

def removeLine(i):
	global M
	del a[i]
	M -= 1

def deleteMins(min):
	global M, N, a
	i = 0
	j = 0
	#remove lines
	while i<M:
		j = 0
		while (j<N and a[i][j] == min):
			j+=1
		if(j == N): 
			removeLine(i)
		else: i+=1
	i = 0
	j = 0
	while j<N:
		i = 0
		while (i<M and a[i][j] == min):
			i+=1
		if(i == M):
			removeCol(j)
		else: j+=1

for x in xrange(1,Q+1):
	line = raw_input()
	line = line.split()
	M = int(line[0])
	N = int(line[1])
	a = list(list(0 for i in xrange(0,N)) for j in xrange(0,M))
	for i in xrange(0,M):
		line = raw_input()
		line = line.split()
		for j in xrange(0,N):
			a[i][j] = int(line[j])
	lastMin = 100
	min = extractmin()
	while lastMin != min:
		deleteMins(min)
		lastMin = min
		min = extractmin()
	if min == 0: 
		print "Case #%d: YES" % x
	else: 
		print "Case #%d: NO" % x


			