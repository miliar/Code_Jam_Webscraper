import re

L, D, N = map(int, raw_input().split())
text = ""
for i in xrange(D): text+=raw_input().strip()+"\n"
for i in xrange(N):
	pat = "^"+raw_input().strip().replace('(', '[').replace(')', ']')+"$"
	print "Case #%d: %d" % (i+1, len(re.findall(pat, text, re.MULTILINE)))
