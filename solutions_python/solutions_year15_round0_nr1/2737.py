def solution(shyness_levels):
	additional = 0
	standing = 0

	for i, x in enumerate(shyness_levels):
		if i <= standing:
			standing += x
		elif x > 0:
			needed = (i - standing)
			additional += needed
			standing += x + needed
	return additional

if __name__ == '__main__':
	cases = int(raw_input())
	for x in xrange(0, cases):
		case = raw_input()
		number, shyness_levels = case.split(" ")
		print "Case #%i: %i" % (x + 1, solution(map(int, shyness_levels)))
