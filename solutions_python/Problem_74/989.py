import sys

f = open(sys.argv[1])
T = int(f.readline().strip())

for i in xrange(T):
	tokens = f.readline().strip().split(' ')
	N = int(tokens.pop(0))

	O = []
	B = []
	order = []
	for j in xrange(N):
		color = tokens.pop(0)
		order.append(color)
		if color == 'O':
			O.append(int(tokens.pop(0)))
		elif color == 'B':
			B.append(int(tokens.pop(0)))
		else:
			raise Exception('Invalid input')

	time = 0
	b = 1
	o = 1
	while len(order) > 0: 
		pressed = False
		if len(B) > 0:
			if B[0] < b:
				b -= 1
			elif B[0] > b:
				b += 1
			elif order[0] == 'B':
				B.pop(0)
				pressed = True
		if len(O) > 0:		
			if O[0] < o:
				o -= 1
			elif O[0] > o:
				o += 1
			elif order[0] == 'O':
				O.pop(0)
				pressed = True

		if pressed:
			order.pop(0)
		time += 1

	print 'Case #%d: %d' % (i+1, time)	


