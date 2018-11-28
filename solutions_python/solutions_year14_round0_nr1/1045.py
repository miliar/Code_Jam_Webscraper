T = int(raw_input())

for i in xrange(T):
	n = int(raw_input())
	n -= 1
	first = []
	for j in xrange(4):
		first.append(map(int,raw_input().split()))
	
	second = []
	m = int(raw_input())
	m -= 1
	for j in xrange(4):
		second.append(map(int,raw_input().split()))



	same = 0

	number = 0

	for j in xrange(4):
		if first[n][j] in second[m]:
			same += 1
			number = first[n][j]
	

	print "Case #" + str(i+1) + ":",
	if same == 0:
		print 'Volunteer cheated!'
	elif same == 1:
		print number
	else :
		print 'Bad magician!'

	



