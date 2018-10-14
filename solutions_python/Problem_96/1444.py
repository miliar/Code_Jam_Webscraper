import sys

lines = open(sys.argv[1], 'rt').readlines()

count = 1
for l in lines[1:]:
	ss = l.strip()

	items = ss.split(' ')

	N = int(items[0])
	S = int(items[1])
	p = int(items[2])

	result = 0

	for i in range(3, len(items)):
		ti = int(items[i])
		
		if ti < p:
			continue

		if 3 * p - 2 <= ti:
			result += 1
		else:
			if (3 * p - 4 <= ti) and (S > 0):
				S -= 1
				result += 1

	print 'Case #%d: %d' % (count, result)
	
	count += 1