import sys

t = int(sys.stdin.readline())

for count in range(1, t+1):
	num = int(sys.stdin.readline())
	values = sys.stdin.readline()
	tokens = values.split()
	
	values = map(int, tokens)
	values2 = map(int, tokens)

	values2.sort()

	diff = 0
	for i in range(0, len(values)):
		if values[i] != values2[i]:
			diff += 1
	
	print "Case #" + str(count) + ":", diff
print 
