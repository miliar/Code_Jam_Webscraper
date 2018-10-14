def isPar(x):

	s = "%d" % x
	for i in range(len(s)):
		if(s[i] != s[-1 - i]):
			return False
	return True

def makeParList():

	ret = []

	for i in range(1, 12000000):

		if(isPar(i) and isPar(i * i)):
			ret.append(i)

	return ret

casenum = int(raw_input())
parlist = makeParList()

for testcase in range(1, casenum + 1):

	a, b = map(int, raw_input().split(" "))
	count = 0

	for i in parlist:

		if(i * i >= a and i * i <= b):
			count += 1

	print "Case #%d: %d" % (testcase, count)