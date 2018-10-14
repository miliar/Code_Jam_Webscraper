string = "welcome to code jam"
L = 19

pd = None

def count_occurrences(matrix,n,L,min):
	count = 0
	if n == L:
		return 1
	if pd[n].has_key(min) and pd[n][min] != -1:
		return pd[n][min]
	for el in matrix[n]:
		if el >= min:
			#print el,n
			count += count_occurrences(matrix,n+1,L,el+1)
	pd[n][min] = count
	return count

def transform(n):
	n = str(n)[-4:]
	while(len(n)<4):
		n = "0"+n
	return n

n = int(raw_input())
for i in xrange(n):
	s = raw_input().lower()
	size = len(s)
	count = 0
	matrix = [[] for h in xrange(L)]
	pd = [{} for h in xrange(L)]

	for j in xrange(size):
		for k in xrange(L):
			if s[j] == string[k]:
				matrix[k].append(j)
				pd[k][j] = -1
	#print matrix
	print "Case #"+str(i+1)+":",transform(count_occurrences(matrix,0,19,0))

	'''
	lasts = [-1 for h in xrange(L)]
	l_i = size-1
	for l in xrange(len(string[::-1])):
		for k in xrange(l_i,0,-1):
			if s[k] == string[L-l-1]:
				lasts[L-l-1] = k
				l_i = k-1
				break
	print lasts
	if lasts[0] == -1:
		print "Case #"+str(i+1)+": 0000"
		continue
	'''
