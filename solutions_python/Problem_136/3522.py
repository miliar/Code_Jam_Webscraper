import sys
sys.setrecursionlimit(2000)

def s(t, r, c, f, x):
	if x/r < c/r + x/(r+f):
		return t + x/r
	else:
		return s(t+c/r, r+f, c, f, x)
	
t = int(input())

for case in range(t):
	in_var = raw_input()
	c, f, x, = in_var.split()
	c = float(c)
	f = float(f)
	x = float(x)
	print("Case #" + str(case+1) + ": " + str(s(0.0, 2.0, c, f, x)))
