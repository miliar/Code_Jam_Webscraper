import sys

def cal():
	r, c = [int(x) for x in raw_input().strip().split()]
	lines = list()
	r_count = 0
	while r_count < r:
		lines.append([x for x in raw_input().strip()])
		r_count += 1
	r_count = 0
	while r_count < r:
		c_count = 0
		while c_count < c:
			if lines[r_count][c_count] == '#':
				lines[r_count][c_count] = '/'
				if (r_count < r - 1 and lines[r_count + 1][c_count] == '#') and (c_count < c - 1 and lines[r_count][c_count + 1] == '#') and (r_count < r - 1 and c_count < c - 1 and lines[r_count + 1][c_count + 1] == '#'):
					lines[r_count + 1][c_count] = '\\'
					lines[r_count][c_count + 1] = '\\'
					lines[r_count + 1][c_count + 1] = '/'
				else:
					return False
			c_count += 1
		r_count += 1
	return lines


t = int(raw_input().strip())
t_count = 1
while t_count <= t:
	ans = cal()
	print 'Case #%d:' % (t_count,)
	if not ans:
		print 'Impossible'
	else:
		for a in ans:
			for b in a:
				sys.stdout.write(b)
			print
	t_count += 1

