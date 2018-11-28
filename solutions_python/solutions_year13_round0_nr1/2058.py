def row(c,l):
	i = 0
	j = 0
	flag = 0
	while(i<4):
		if l[i][j] == c or l[i][j] == 'T':
			j += 1
			flag = 1 
		else:
			j = 0
			i += 1
			flag = 0
		if j == 4:
			break
	return flag

def col(c,l):
	i = 0
	j = 0
	flag = 0
	while(j<4):
		if l[i][j] == c or l[i][j] == 'T':
			i += 1
			flag = 1
		else:
			i = 0
			j += 1
			flag = 0
		if i == 4:
			break
	return flag

def diag1(c,l):
	i = 0
	j = 0
	flag = 0
	while(i<4):
		if l[i][j] == c or l[i][j] == 'T':
			j += 1
			i += 1
			flag = 1
		else:
			flag = 0
			break
	return flag

def diag2(c,l):
	i = 0
	j = 3
	flag = 0
	while(i < 4):
		if l[i][j] == c or l[i][j] == 'T':
			i += 1
			j -= 1
			flag = 1
		else:
			flag = 0
			break
	return flag

def cond(c,l):
	if row(c,l) == 1 or col(c,l) == 1 or diag1(c,l) == 1 or diag2(c,l) == 1:
		return 1
	else:
		return 0

t = int(raw_input())
for i in range(t):
	if i >= 1:
		s = raw_input()
	l = []
	dc = 0
	for j in range(4):
		s = raw_input()
		if s != '\n':
			dc += s.count('.')
			l.append(s)
	if cond('X',l)  == 1:
		print "Case #%i: X won"%(i+1)
	elif cond('O',l) == 1:
		print "Case #%i: O won"%(i+1)
	elif dc == 0:
		print "Case #%i: Draw"%(i+1)
	else:
		print "Case #%i: Game has not completed"%(i+1)
