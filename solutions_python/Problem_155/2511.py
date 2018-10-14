import sys

def test(test_num, s_max, ss):
	n = 0
	s = 0
	for i in range(0, s_max+1):
		add = 0
		if s < i:
			add = i - s
		s += add
		s += int(ss[i])
		n += add
	print("Case #%d: %d" % (test_num, n))

def tests(f):
	t = int(f.readline())
	for t in range(t):
		line = f.readline()
		while line[-1] == '\r' or line[-1] == '\n':
			line = line[:-1]
		s_max,ss = line.split(' ')
		test(t + 1, int(s_max), ss)

with open("A-large.in") as f:
	tests(f)
