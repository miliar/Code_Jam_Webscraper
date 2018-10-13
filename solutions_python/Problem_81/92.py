def computerpi(mat):
	n = len(mat)
	nw = [0 for i in range(n)]
	nl  = [0 for i in range(n)]
	for i in range(n):
		for j in range(n):
			if mat[i][j] == '1':
				nw[i] += 1
			elif mat[i][j] == '0':
				nl[i] += 1
	rpi = [0 for i in range(n)]
	wp = map(lambda x,y: x*1./(x+y),nw,nl)
	owp = [0 for i in range(n)]
	for i in range(n):
		for j in range(n):
			if mat[i][j] == '1':
				owp[i] += nw[j]/(nw[j]+nl[j]-1.)
			elif mat[i][j] == '0':
				owp[i] += (nw[j] - 1.) / (nw[j]+nl[j] - 1.)
		owp[i] /= (nw[i] + nl[i])
	oowp = [0 for i in range(n)]
	for i in range(n):
		for j in range(n):
			if mat[i][j] != '.':
				oowp[i] += owp[j]
		oowp[i] /= (nw[i] + nl[i])
	rpi = map(lambda x,y,z: .25 * x + .5 * y + .25 * z,wp,owp,oowp)
	for x in rpi:
		print x
		
def solverpi():
	f = open('gcjdata.txt','r')
	lines = f.readlines()
	i = 1
	j = 1
	while i < len(lines):
		n = int(lines[i])
		print "Case #{0}:".format(j)
		computerpi(lines[i+1:i+n+1])
		i += n+1
		j += 1
solverpi()