


def solve(m):

	still = False
	m1 = zip (*m)
	matrix = m + m1 + [[m[0][0],m[1][1],m[2][2],m[3][3]]] + [[m[0][3],m[1][2],m[2][1],m[3][0]]]
	print (matrix)
	for i in range(10):
		s = sum(matrix[i])
		if ( (s % 5 == 0 and s <= 20 ) ):
			return "X won"
		elif((s % 2 == 0 and s <= 8 ) ):
			return "O won"
		elif( s >= 30 and (s % 5 == 0 or s % 2 ==0)  ):
			still =  True

	if(still):
		return "Game has not completed"
	else:
		return "Draw"



f = open('inputs', 'r')
o = open('outputs', 'w')

T = int(f.readline().strip())

for t in xrange(T):
	case = []
	for i in range(4):
		items = list(f.readline().strip())
		li = []
		for item in items:
			if (item == '.'):
				li.append(30)
			elif (item == 'X'):
				li.append(5)
			elif (item == 'O'):
				li.append(2)
			elif (item == 'T'):
				li.append(0)
			else:
				print("erro")
		case.append(li)
	f.readline()
	s = "Case #%d: %s\n" % (t+1, solve(case))
	o.write(s)
	print(s)
f.close()
o.close()	
