f1 = open('q2.in', 'r')
f2 = open('q2.out', 'w')
no_cases = f1.readline().strip()
for x in range(0, int(no_cases)):
	num  = f1.readline().strip()
	f = 2
	(C, F, X) = num.split()
	C = float(C)
	F = float(F)
	X = float(X)
	ans = float(0)
	while ( (X/(f+F)) + (C/f) < (X/f) ):
		ans = ans + (C/f)
		f = f + F
	ans = ans + (X/f)
	f2.write("Case #"+str(x+1)+": "+str(ans)+"\n")
