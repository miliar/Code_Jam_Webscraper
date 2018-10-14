filename = 'B-small-attempt2.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t, 
	AC,AJ = map(int,f.readline().split())
	C = []
	J = []
	for i in range(AC):
		C.append(map(int,f.readline().split()))
	for i in range(AJ):
		J.append(map(int,f.readline().split()))
	C.sort()
	J.sort()
	if len(C) == 2:
		if C[1][1]-C[0][0] <= 720:
			print "2"
		elif C[0][1] + 1440 - C[1][0] <= 720:
			print "2"
		else:
			print "4"
	elif len(J) == 2:
		if J[1][1]-J[0][0] <= 720:
			print "2"
		elif J[0][1] + 1440 - J[1][0] <= 720:
			print "2"
		else:
			print "4"
	else:
		print "2"