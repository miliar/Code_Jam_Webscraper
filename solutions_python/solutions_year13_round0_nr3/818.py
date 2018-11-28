def isPal(s):
	for i in xrange(len(s)/2):
		if s[i] != s[-i-1]:
			return False
	return True

try:
	nTests = int(raw_input())
	limit = 10**14
	mem = [i*i for i in xrange(int(limit**0.5)+1) if isPal(str(i)) and isPal(str(i*i))]

	for test in xrange(1, nTests+1):
		a,b = map(int, raw_input().split())

		iniInd = 0
		end = len(mem)
		while iniInd < end and a > mem[iniInd]:
			iniInd += 1

		endInd = iniInd
		while endInd < end and b >= mem[endInd]:
			endInd += 1

		print "Case #%d: %s" % (test, str(endInd-iniInd))

except EOFError:
	pass
