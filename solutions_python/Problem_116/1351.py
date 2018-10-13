lines = open('A-large.in').read().split('\n')

n = int(lines[0])
lines = lines[1:]


def winner(alist, ch):
	return alist.count(ch)+alist.count('T')==4

def won(a, ch):
	d1 = [a[i][i] for i in range(4)]
	if winner(d1, ch):
		return True
	d2 = [a[i][4-i-1] for i in range(4)]
	if winner(d2, ch):
		return True
	for i in range(4):
		row = list(a[i])
		if winner(row, ch):
			return True
		column = [a[j][i] for j in range(4)]
		if winner(column, ch):
			return True			
	return False

def notfinished(a):
	for x in a:
		if '.' in x:
			return True
	return False

f2 = open('1.out', 'w')
for t in range(n):
	s = 'Case #'+str(t+1)+': '
	a = lines[t*5:t*5+4]
	if won(a, 'X'):
		s+='X won'
	elif won(a,'O'):
		s+='O won'
	elif notfinished(a):
		s+='Game has not completed'
	else:
		s+='Draw'
	f2.write(s+'\n')

