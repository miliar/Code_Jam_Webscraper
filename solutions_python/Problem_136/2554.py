import sys

lines = sys.stdin.readlines()

T = int(lines.pop(0))

for i in range(0, T):
	(C,F,X) = [float(x) for x in lines[i].split(" ")]

	P = 2
	t = 0.0

	while X*F > C * (P + F):
		t += C/P
		P += F

	t += X/P

	print("Case #%d: %.8f" % (i+1, t))