import sys
inp = sys.stdin
T = int(inp.readline())

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

def read_floats():
	return [float(x) for x in raw_input().strip().split()]

for t in range(1, T+1):
	print 'Case #'+str(t)+':',
	C,F,X = read_floats()
	rate = 2.0
	if X <= C:
		print X/rate
		continue
	t = 0
	while 1:
	  t += C/rate
	  if (X-C)/rate <= X/(rate+F): break
	  rate += F
	t += (X-C)/rate
	print t