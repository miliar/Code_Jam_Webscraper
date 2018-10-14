import re
import sys

if __name__ == '__main__':
	# L D N
	wordlen, dictlen, ntests = map(int,sys.stdin.readline().strip().split())

	words = [sys.stdin.readline().strip() for i in xrange(dictlen)]

	for case in xrange(1,ntests+1):
		pattern = sys.stdin.readline().strip()

		# Convert into a regexp and compile
		pattern = pattern.replace('(','[').replace(')',']')
		pattern = re.compile("^" + pattern + "$")

		# Count the matches (yeah, yeah, could do this in 1 big string)
		n = sum(1 for word in words if re.match(pattern,word) != None)
		print "Case #%d: %d" % (case,n)
