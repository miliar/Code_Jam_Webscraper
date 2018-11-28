from collections import defaultdict

def split(n):
	m = max(n)
	for i in range(len(n)):
		if n[i] == m:
			x = (m-1)/2
			return n[:i] + [x, m-1-x] + n[i+1:]

def last(seats, p):
	m = max(seats.keys())
	a = (m-1)/2
	b = m - 1- a
	s = seats[m]
	if seats[m] >= p:	
	    return max(a,b), min(a,b)
	else:
		seats[a] += s
		seats[b] += s
		del seats[m]
		p -= s
		return last(seats, p)


def find_last(x, y):
	x = [x]
	for i in range(y-1):
		x = split(x)
	m = max(x)
	a = (m-1)/2
	b = m - 1- a
	return max(a,b), min(a,b)


if __name__ == '__main__':
	import sys
	lines = open(sys.argv[1]).readlines()[1:]
	for i in range(len(lines)):
		x, y = lines[i].strip().split()
		seats = defaultdict(int)
		seats[int(x)] = 1
		a, b = last(seats, int(y))
		print 'Case #{}: {} {}'.format(i+1, a, b)