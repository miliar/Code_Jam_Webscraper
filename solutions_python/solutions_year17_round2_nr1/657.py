import sys

if len(sys.argv) == 2:
	inp = sys.argv[1]
	assert(inp[-3:] == '.in')
	outp = inp[:-3] + '.out'
	
	sys.stdin = open(inp, 'r')
	sys.stdout = open(outp, 'w')
	

T = int(sys.stdin.readline())
for case_number in range(1, T+1):
	D, N = map(int, sys.stdin.readline().split(' '))
	
	H = []
	for i in range(N):
		k, s = map(int, sys.stdin.readline().split(' '))
		H.append((k, s))
	H = sorted(H, reverse=True)

	t = 0
	for k, s in H:
		t = max(t, (float(D) - k)/s)

	print("Case #{}: {}".format(case_number, float(D)/t))
