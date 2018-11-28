of = None

def do(i, l):

	#Actually do something

	print 'Doing '+str(i)

	zeros = False

	d = diagonals(l)
	if d == 1 or d == 2:
		out(i, d)
		return
	elif d == 0:
		zeros = True

	c = columns(l)
	if c == 1 or c == 2:
		out(i, c)
		return
	elif c == 0:
		zeros = True

	r = rows(l)
	if r == 1 or r == 2:
		out(i, r)
		return
	elif r == 0:
		zeros = True

	if zeros:
		out(i, 0)
	else:
		out(i, 3)


	

	

def check(ma):
	r = 3
	

	for m in ma:
		i = ma.index(m)

		if m == 0:
			return 0

		if r == 3:
			r = m
		
		elif m == 1:
			if not r == 1:
				return 3
		elif m == 2:
			if not r == 2:
				return 3

	if r == 1 or r == 2:
		return r

def diagonals(ma):

	m = []
	mi = []
	for i in range(0, 4): 
		
		m.append(ma[i][i])
		mi.append(ma[i][3-i])

	zs = False
	d1 = check(m)
	if d1 == 1 or d1 == 2:
		return d1
	elif d1 == 0:
		zs = True

	d2 = check(mi)
	if d2 == 1 or d2 == 2:
		return d2
	elif d2 == 0:
		zs = True

	if zs:
		return 0
	
	return 3

def columns(ma):

	zero = False
	for i in range(0, 4):
		m = []
		for a in range(0,4):
			m.append(ma[a][i])
		print str(m)
		a = check(m)
		if a == 1 or a == 2:
			return a
		elif a == 0:
			zero = True
	if zero:
		return 0
	return 3

def rows(ma):

	zero = False
	for i in range(0, 4):
		m = []
		for a in range(0,4):
			m.append(ma[i][a])
		print str(m)
		a = check(m)
		if a == 1 or a == 2:
			return a
		elif a == 0:
			zero = True
	if zero:
		return 0
	return 3

	
	


def out(i, o):

	if o == 0:
		oo = 'Game has not completed'
	elif o == 1:
		oo = 'X won'
	elif o == 2:
		oo = 'O won'
	elif o == 3:
		oo = 'Draw'

	of.write('Case #'+str(i)+': '+oo+'\n')



if __name__ == '__main__':
	fn = raw_input('Input file path:')
	f = open(fn) 
	ls = f.readlines()
	of = open('large.out', 'w+')
	lss = []

	for i in range(1, (int(ls[0])+1)):
		a = i-1
		lss.append(1+a*5)

	
	for i in lss:

		
		ma = []
		for a in range(i, i+4):

			maa = []
			ss = ls[a]
			

			s = list(ss)
			
			for sa in s:
				if sa == 'X':
					maa.append(1)
				elif sa == 'O':
					maa.append(2)
				elif sa == 'T':
					maa.append(3)
				elif sa == '.':
					maa.append(0)
				
			ma.append(maa)
		do(lss.index(i)+1, ma)




	of.close()

	