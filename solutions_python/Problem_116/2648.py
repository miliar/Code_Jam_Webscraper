import sys

c1 = (1<<0)+(1<<5)+(1<<10)+(1<<15)
c2 = (1<<3)+(1<<6)+(1<<9)+(1<<12)

c = (1<<0)+(1<<4)+(1<<8)+(1<<12)
r = (1<<0)+(1<<1)+(1<<2)+(1<<3)

def check(x,y):
	a = c
	b = r

	#check corners
	if x & c1 == c1:
		return 'X won'
	if x & c2 == c2:
		return 'X won'
	if y & c1 == c1:
		return 'O won'
	if y & c2 == c2:
		return 'O won'

	for i in range(4):
		if x & a == a:
			return 'X won'
		if x & b == b:
			return 'X won'
		if y & a == a:
			return 'O won'
		if y & b == b:
			return 'O won'
		a = a << 1
		b = b << 4

	if (x | y) == ((1 << 16) - 1):
		return 'Draw'

	return 'Game has not completed'

T = int(sys.stdin.readline())

for k in range(T):
	x = 0
	y = 0
	i = 0
	for j in range(4):
		l = sys.stdin.readline()[:-1]
		for item in l:
			if item == 'X':
				x += 1 << i
			elif item == 'O':
				y += 1 << i
			elif item == 'T':
				x += 1 << i
				y += 1 << i
			i += 1

	sys.stdout.write("Case #%d: " % (k+1))
	print check(x,y)
	sys.stdin.readline()

