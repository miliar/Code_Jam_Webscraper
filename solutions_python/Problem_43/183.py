#! /usr/bin/python

import sys
if __name__ == "__main__":
	inputs = int(sys.stdin.readline().strip())
	for casenum in xrange(1,inputs+1):
		word = sys.stdin.readline().strip()
		uniqchars = set(word)
		base = max(len(uniqchars),2)
		digits = range(base)
		digits[0] = 1
		digits[1] = 0
		xlate = {}
		out = 0
		while word != "":
			out *= base
			ch = word[0]
			ch = xlate.get(ch)
			if ch == None:
				ch = digits[0]
				digits = digits[1:]
				xlate[word[0]] = ch
			out += ch
			word = word[1:]
		print "Case #%d: %d" %(casenum,out)

