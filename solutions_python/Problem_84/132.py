f = open("in", "rb")
t = int(f.readline())
def ok(i,j):
	if l[i+1][j+1]!='#' or l[i+1][j]!='#' or l[i][j+1]!='#':
		raise Exception('1')
	return True
	
for tt in range(t):
	print "Case #"+str(tt+1)+":"
	r,c = map(int, f.readline().split())
	l = []
	for i in range(r):
		l += [list(f.readline().strip())]
	try:
		for i in range(r):
			for j in range(c):
				if l[i][j] == '#':
					if ok(i,j):
						l[i][j] = '/'
						l[i+1][j+1] = "/"
						l[i+1][j] = '\\'
						l[i][j+1] = '\\'
		for i in range(r):
			print ''.join(l[i])
	except:
		print "Impossible"
