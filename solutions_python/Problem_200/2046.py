import sys
sys.setrecursionlimit(10000)


file = open('B-large.in','r')
testCases = int(file.readline())


def checkNumber(head, tail, keep):
	# is already sorted
	if len(tail) <= 0:
		return 0

	# increase the head
	elif head == int(tail[0]):
		if len(keep) <= 0:
			return checkNumber(int(tail[0]), tail[1:], tail)
		else:
			return checkNumber(int(tail[0]), tail[1:], keep)

	if head < int(tail[0]):
		return checkNumber(int(tail[0]), tail[1:], [])

	else:
		if len(keep) <= 0:
			return int(tail) + 1
		else:
			return int(keep) + 1		

for i in range(0,testCases):
	line = file.readline().strip()
	res = checkNumber(int(line[0]), line[1:], [])

	print 'Case #' + str(i+1) + ': ' + str(int(line) - res)

