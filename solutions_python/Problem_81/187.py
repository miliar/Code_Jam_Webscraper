f = open("in", "rb")
tt = int(f.readline())
l = []
def avg(ll, i):
	summ = 0
	ssh = 0
	for j in range(len(ll)):
		if (j!=i):
			if ll[j] != '.':
				ssh += 1
				summ += int(ll[j])
	return float(summ)/ssh
def tong(ll):
	t = 0.0
	for i in ll:
		if i != '.':
			t += int(i)
	return t
def sssh(ll):
	t = 0.0
	for i in ll:
		if i != '.':
			t += 1
	return t
for t in range(tt):
	n = int(f.readline())
	l = []
	wp = [0.0]*n
	owp = [0.0]*n
	oowp = [0.0]*n
	for i in range(n):
		l += [list(f.readline().strip())]
	for i in range(n):
		wp[i] = tong(l[i])/sssh(l[i])
		tg = 0.0
		for j in range(n):
			if i!=j and l[i][j]!='.':
				tg += avg(l[j],i)
		owp[i] = tg / sssh(l[i])
	for i in range(n):
		tg = 0.0
		ssh = 0
		for j in range(n):
			if l[i][j]!='.':
				tg += owp[j]
				ssh += 1
		oowp[i] = tg/ssh
	print "Case #"+str(t+1)+":"
	for i in range(n):
		print 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]
