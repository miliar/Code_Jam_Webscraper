import sys, math

tt=input()
for i in range(tt):
	R = 2.0
	C, F, X = sys.stdin.readline().rstrip().split(" ")
	C = float(C)
	X = float(X)
	F = float(F)
	n = X/C - R/F - 1
	if n > 0:
		n = math.ceil(n)
	else:
		n = 0
	ans = 0.0
	for j in range(int(n)):
		ans += C/(R + (j*F))
	ans += X/(R+(n*F))
	sys.stdout.write("Case #%d: %.7f\n" % (i+1, ans))
