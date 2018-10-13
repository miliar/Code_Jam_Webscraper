# Problem A. Magic Trick
# Qualification Round
 
# Author: Phuriphat Boontanon

import sys

if not len(sys.argv):
	print '[.] No input file'
	sys.exit()

input = open(sys.argv[1], 'r+')
n = int(input.readline())
for k in range(1, n+1):
	a1 = int(input.readline())
	r1 = []
	for i in range(0, 4):
		r1.append(input.readline().split())
		r1[i] = [int(x) for x in r1[i]]
	a2 = int(input.readline())
	r2 = []
	for i in range(0, 4):
		r2.append(input.readline().split())
		r2[i] = [int(x) for x in r2[i]]
	answer = []
	for i in range(0, 4):
		if r1[a1-1][i] in r2[a2-1]:
			answer.append(r1[a1-1][i])
	nanswer = len(answer)
	if not nanswer:
		print 'Case #%d: Volunteer cheated!'%(k)
	elif nanswer == 1:
		print 'Case #%d: %d'%(k,answer[0])
	else:
		print 'Case #%d: Bad magician!'%(k)
	