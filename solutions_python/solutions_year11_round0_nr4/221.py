import sys
import itertools

file = open(sys.argv[1])
out = open('out.txt', 'w')

N = int(file.readline())
print 'Total ', N, ' cases'

case = 1

while case <= N:
#	print case
	final = 0
	m = int(file.readline())
	values = map(lambda x: int(x), file.readline().split())
#	print values
	count = 0
	for i in range(m):
		if i + 1 != values[i]:
			count += 1
	print case, float(count)
	out.write('Case #' + str(case) + ': ' + str(count) + '\n')
	case += 1
