from sys import stdin

N = int(stdin.readline())

for n in xrange(N):
	line = stdin.readline().split(' ')
	shyest = int(line[0])
	answer = 0
	total_people = 0
	for level, number in enumerate(line[1]):
		if (not number.isdigit()):
			break
		if total_people < level:
			answer += level-total_people
			total_people += level-total_people
		total_people += int(number)
	
	print "Case #%d: %d" % (n+1, answer)
