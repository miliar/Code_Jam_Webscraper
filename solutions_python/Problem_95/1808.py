import sys
A = {}
def prepare():
	for i in range(3):
		s1 = raw_input()
		s2 = raw_input()
		for i in range(len(s1)):
			A[s1[i]] = s2[i]
	A['z'] = 'q'
	A['q'] = 'z'

prepare()
x = (int)(raw_input())
for i in range(x):
	s = raw_input()
	print "Case #%d: " % (i+1),
	for i in s:
		sys.stdout.write(A[i])
	print


