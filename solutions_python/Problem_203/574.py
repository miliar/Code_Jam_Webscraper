def lcoccupied(a, i, j, lc, ur, br):
	if (lc-1 < 0): return True
	for m in range(ur, br+1):
		if (a[m][lc-1] != None): 
			return True
	return False

def rcoccupied(a, i, j, rc, ur, br):
	if (rc+1 >= len(a[0])): return True
	for m in range(ur, br+1):
		if (a[m][rc+1] != None): 
			return True
	return False

def uroccupied(a, i, j, ur, lc, rc):
	if (ur-1 < 0): return True
	for m in range(lc, rc+1):
		if (a[ur-1][m] != None): 
			return True
	return False

def broccupied(a, i, j, br, lc, rc):
	if (br+1 >= len(a)): return True
	for m in range(lc, rc+1):
		if (a[br+1][m] != None): 
			return True
	return False

def expand(a, i, j, ur, br, lc, rc):
	if (not lcoccupied(a, i, j, lc, ur, br)):
		return expand(a, i, j, ur, br, lc-1, rc)
	elif (not rcoccupied(a, i, j, rc, ur, br)):
		return expand(a, i, j, ur, br, lc, rc+1)
	elif (not uroccupied(a, i, j, ur, lc, rc)):
		return expand(a, i, j, ur-1, br, lc, rc)
	elif (not broccupied(a, i, j, br, lc, rc)):
		return expand(a, i, j, ur, br+1, lc, rc)
	else:
		return (ur, br, lc, rc)

def fill(a, ur, br, lc, rc, e):
	for i in range(ur, br+1):
		for j in range(lc, rc+1):
			a[i][j] = e
	return a

T = int(raw_input())
for i in xrange(1, T+1):
	initials = set()
	r, c = [int(x) for x in raw_input().split(" ")]
	a = [[None] * c for n in range(r)]
	for j in range(r):
		a[j] = [s for s in raw_input()]
		for k in range(c):
			if a[j][k] == "?": a[j][k] = None

	for j in range(r):
		for k in range(c):
			if (a[j][k] != None and a[j][k] not in initials):
				(ur, br, lc, rc) = expand(a,j,k,j,j,k,k)
				a = fill(a, ur, br, lc, rc, a[j][k])
				initials.add(a[j][k])

	cake = ""	
	for j in range(r):
		for k in range(c):
			cake += a[j][k]
		cake+="\n"
	print "Case #{}: \n{}".format(i, cake)