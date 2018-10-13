import sys, string

N = int(raw_input())
table = string.maketrans(string.ascii_lowercase,
	"yhesocvxduiglbkrztnwjpfmaq")

for case_num in xrange(1, N+1):
	line = raw_input()
	decoded = string.translate(line, table)
	print "Case #%d: %s" % (case_num, decoded)