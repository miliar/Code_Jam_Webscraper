

f = open('in','r')
T = int(f.readline())
for t in xrange(T):
	R = [0] * 10
	r = -1 
	c = -1
	for i in xrange(4):
		l = f.readline()
		for j in xrange(4):
			if l[j] == 'O':
				R[i] += 1
				R[j+4] += 1
				if i==j: R[8] += 1
				if i+j == 3: R[9] += 1
				continue
			if l[j] == 'T':
				r = i
				c = j
				continue
			if l[j] == '.':
				R[i] += 1000
				R[j+4] += 1000
				if i==j: R[8] +=1000
				if i+j == 3: R[9] += 1000
	f.readline()
	out = False
	for i in xrange(10):
		if R[i] == 0: 
			print 'Case #'+str(t+1)+': X won'
			out = True
			break

	if out: continue

	if r>=0 and c>=0:
		R[r] += 1
		R[4+c] += 1
		if r==c: R[8] += 1
		if r+c == 3: R[9] += 1
	for i in xrange(10):
		if R[i] == 4:
			print 'Case #'+str(t+1)+': O won'
			out = True
			break

	if out: continue

	for i in xrange(10):
		if R[i] >= 1000:
			print 'Case #' + str(t+1)+': Game has not completed'
			break
	else:
		print 'Case #' + str(t+1)+ ': Draw'
	
		
