f = open('D-large.in')
fw = open('D-large-output.txt', 'w')

cases = int(f.readline())
for case in range(cases):
	N = int(f.readline())
	X = map(float, f.readline().split())
	Y = map(float, f.readline().split())
	
	Z = []
	for value in X:
		Z.append((value, 'A'))
	for value in Y:
		Z.append((value, 'B'))

	X.sort()
	Y.sort()
	Z.sort()
	
	dec_war = 0
	for i in range(N):
		if X[0] > Y[0]:
			dec_war += 1
			del X[0]
			del Y[0]
		else:
			del X[0]
			del Y[-1]
	print dec_war

	war = 0
	Z.reverse()
	acc = 0
	for pair in Z:
		if pair[1] == 'A':
			if acc == 0:
				war += 1
			else:
				acc -= 1
		else:
			acc += 1
	print war

	fw.write('Case #' + str(case + 1) + ': ' + str(dec_war) + ' ' + str(war) + '\n')

fw.close()
f.close()
