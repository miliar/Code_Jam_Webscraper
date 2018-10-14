import sys

handle = open(sys.argv[1])
n = int(handle.readline())
for c in xrange(n):
	shyness = [int(x) for x in handle.readline().split()[1]]
	answer = 0
	previous = 0
	for i, si in enumerate(shyness):
		if previous >= i:
			previous += si
		else:
			answer += i - previous
			previous = i + si
	print "Case #" + str(c + 1) + ":", answer
