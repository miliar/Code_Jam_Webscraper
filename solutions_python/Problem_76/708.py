

fp = open('C-large.in', 'r')
n = int(fp.next())

case = 1

for line in fp:
	result = -1
	line = sorted(fp.next().split())
	line = [int(x) for x in line]
	
	xorall = reduce(lambda x, y: x ^ y, line)
	
	for x in range(len(line)):
		if xorall ^ line[x] == line[x]:
			if sum(line) - line[x] > result:
				result = sum(line) - line[x]
	
	if result == -1:
		print 'Case #' + str(case) + ': NO'
	else:
		print 'Case #' + str(case) + ':', result

	case += 1
	
