import sys
T = int(sys.stdin.readline())
for testcase in range(1, T + 1):
	N = int(sys.stdin.readline())
	wires = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]
	count = 0
	while len(wires):
		a = wires.pop()
		for b in wires:
			if (a[0] < b[0]) != (a[1] < b[1]):
				count += 1
	print('Case #%d: %d' % (testcase, count))