'''
Ominous omino 4-11-15
This stupid program can only solve the small haha
'''

fin = open('ominousomino.in','r')
fout = open('ominousomino.out','w')

T = int(fin.readline())

for caseno in range(T):
	X, R, C = [int(x) for x in fin.readline().split()]

	#False is Gabriel wins (CAN PLACE), True is Richard wins (ONE WAY CANNOT PLACE)
	if (X == 1):
		result = False
	elif (X == 2):
		result = (R*C % 2 != 0)
	elif (X == 3):
		if (R*C % 3 != 0):
			result = True
		elif (R*C == 3):
			result = True
		else:
			result = False
	elif (X == 4):
		if (R*C % 4 != 0):
			result = True
		elif (R*C == 4):
			result = True
		elif (R*C == 8):
			result = True
		else:
			result = False

	fout.write("Case #" + str(caseno + 1) + ": " + ("RICHARD" if result else "GABRIEL") + '\n')

fin.close()
fout.close()