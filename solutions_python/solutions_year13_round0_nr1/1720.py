#!/usr/bin/python

T = int(raw_input().strip())
for i in range(1, T+1):
	A = [list(raw_input().strip()) for j in range(0,4) ]
	raw_input()
	B = [list(j) for j in zip(*A)]
	C = [ [A[0][0], A[1][1], A[2][2], A[3][3]], [A[0][3], A[1][2], A[2][1], A[3][0]]]
	A.extend(B)
	A.extend(C)
	d = 0
	flag = False
	for row in A:
		x = row.count('X')
		o = row.count('O')
		t = row.count('T')
		d = d + row.count('.')
		if(x == 4 or (x == 3 and t == 1)):
			print "Case #" + str(i) + ": X won"
			flag = True
			break
		elif(o == 4 or ( o == 3 and t == 1)):
			print "Case #" + str(i) + ": O won"
			flag = True
			break
		
	if((not flag) and d > 0):
		print "Case #" + str(i) + ": Game has not completed"
	if((not flag) and d == 0):
		print "Case #" + str(i) + ": Draw"

		




