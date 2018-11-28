from math import *
import re, sys

def solve(S, parts):
	for i,j in zip(S, parts):
		if (len(j)==1 and i!=j) or (len(j)>1 and i not in j[1:-1]):
			return 0
	return 1

if __name__ == "__main__":
	regex = re.compile("([a-z]{1}|\([a-z]+\))")

	l,d,n = (int(i) for i in raw_input().strip().split())
	lst = []
	for i in xrange(d):
		lst.append(raw_input().strip())
	for T in xrange(n):
		inp = raw_input().strip()
		parts = regex.findall(inp)
		ans = sum(solve(i,parts) for i in lst if len(i)==len(parts))
		print "Case #%d: %d" % (T+1, ans)

