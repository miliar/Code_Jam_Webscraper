
testCases = int(input())

for i in xrange(testCases):
	sMax, shynessValues = raw_input().strip().split()
	sMax = int(sMax)

	result = 0
	shy = -1
	standing = 0

	for x in shynessValues:
		shy += 1

		if x == '0':
			continue

		if shy > standing:
			newFriends = (shy - standing)
			result += newFriends
			standing += newFriends

		standing += int(x)

	print ("Case #{0}: {1}".format(i+1, result))
