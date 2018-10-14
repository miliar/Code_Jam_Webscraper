import sys

for i, line in enumerate(sys.stdin):
	if i == 0:
		continue
	print "Case #" + str(i) + ":",
	vals = line.split(' ')
	count = 0
	N = int(vals[0])
	S = int(vals[1])
	p = int(vals[2])
	#1 Regular (non-suprising criteria)
	if p >= 1:
		criteria1 = p + 2*(p-1)
	else:
		criteria1 = -1
	#2 Suprising Criteria
	if p >= 2:
		criteria2 = p+2*(p-2)
	else:
		criteria2 = -1

	for x in range(3, 3 + N):
		#print "Value" + vals[x],
		if int(vals[x]) >= criteria1:
			#print "a",
			count += 1
		elif S > 0 and int(vals[x]) >= criteria2:
			if int(vals[x]) < 2:
				continue
			#print 'b',
			S -= 1
			count += 1
	print count