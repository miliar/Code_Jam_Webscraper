import sys
input = sys.stdin.readlines()
for i in range(1, len(input)):
	tokens = str.rsplit(input[i])
	robot = map(lambda x: x=='B', tokens[1::2])
	dest = map(int, tokens[2::2])
	last = [0, 0]
	pos = [1, 1]
	for r, p in zip(robot, dest):
		last[r] = max(last[not r] + 1, last[r] + abs(pos[r] - p) + 1);
		pos[r] = p
	print 'Case #{0}: {1}'.format(i, max(last))
