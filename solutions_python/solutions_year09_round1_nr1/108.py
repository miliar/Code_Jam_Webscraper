def toBase (n, base):
	digits = "0123456789"

	s = ""
	while True:
		r = n%base
		s = digits[r] + s
		n = n / base
		if n == 0:
			break
	return s

def happy (s,b):
	done = {}

	while s != "1":
		res = 0
		for digit in s:
			res += int(digit)**2
		s = toBase(res,b)
		if s in done: return False

		done[s] = True
	
	return s == "1"

cases = int(raw_input())
for tt in xrange(0,cases):
	bases = map(lambda x: int(x),raw_input().split(' '))

	x = 1
	while True:
		x += 1
		valid = True
		for base in bases:
			if not happy (toBase(x,base),base):
				valid = False
				break
		if valid: break
	print "Case #%d: %d" % (tt+1,x)
