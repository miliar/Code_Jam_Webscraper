from math import floor

def is_palindrome(n):
	s = str(n)
	if 'L' in s:
		s = s[:-1]
	for i in xrange(len(s)/2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True

inputfile = file("C-small-attempt0.in", "rb")
outputfile = file("C-small.out", "wb")
out_s = "Case #%d: %d"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
T, = parse_line()
for ncase in xrange(1, T+1):
    A,B = parse_line()
    count = 0
    for n in xrange(int(floor(A**0.5)), int(floor(B**0.5))+1):
        if A <= n**2 <= B and is_palindrome(n) and is_palindrome(n**2):
            count+=1
    print >>outputfile, out_s % (ncase, count)
