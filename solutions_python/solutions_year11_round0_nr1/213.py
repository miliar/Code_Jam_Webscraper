import sys

file = open(sys.argv[1])
out = open('out.txt', 'w')

N = int(file.readline())

case = 1

def other(h):
	if h == 'O':
		return 'B'
	else:
		return 'O'

def steps(h, n, curr):
#	print h, n, curr
	if h == 'B':
		s = n - curr[0]
		curr[0] = n
	else:
		s = n - curr[1]
		curr[1] = n
#	print s, curr
	return abs(s)

for line in file:
	arr = line.split()
	num = arr[0]
	seq = arr[1:]
	l = len(seq)
	i = 0
	curr = [1, 1]
	prev = ['B', 0]
	total = 0
#	print line, num, seq
	while i < l:
		h = seq[i]
		n = int(seq[i+1])
		s = steps(h, n, curr)
#		print 'Steps: ', s, prev
		if prev[0] == other(h):
			s -= prev[1]
			if s < 0:
				s = 0
			prev = [h, s + 1]
#			print 'Steps: ', s
		else:
			prev[1] = prev[1] + s + 1
		total += s + 1
#		print h, n, i, total
		i += 2
	res = 'Case #' + str(case) + ': ' + str(total) + '\n'
#	print res
	out.write(res)
	case += 1
