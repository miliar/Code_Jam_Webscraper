import fileinput
stdin = fileinput.input()

def solveCase():
	n,s = map(int,stdin.next().split())
	fs = list(map(int,stdin.next().split()))
	fs.sort()
	u = 0
	i = 0
	j = n-1
	while i<j:
		if fs[i]+fs[j]<=s:
			i += 1
		u += 1
		j -= 1
	if i==j:
		u += 1
	return u


for case in xrange(int(stdin.next())):
	print "Case #{0}: {1}".format(case+1,solveCase())
