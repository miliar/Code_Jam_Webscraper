T = int(raw_input())

def toggle(c):
	if c == '+':
		return '-'
	return '+'

def doprob():
	x, y = raw_input().split()
	y = int(y)
	x = list(x)
	ctr = 0
	for i in xrange(len(x)):
		if len(x) - i < y:
			break
		if x[i] == '-':
			for k in xrange(y):
				x[i+k] = toggle(x[i+k])
			ctr += 1
	for k in x:
		if k == '-':
			return "IMPOSSIBLE"
	return ctr

for qq in xrange(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())