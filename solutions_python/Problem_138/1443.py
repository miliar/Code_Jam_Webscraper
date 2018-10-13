#!python2.7
import fileinput
from collections import deque

OFFSET = 3

input_text = []
for line in fileinput.input():
	input_text.append(line.strip())

T = int(input_text[0])

for t in xrange(1, T * OFFSET + 1, OFFSET):
	N = int(input_text[t])
	naomi = sorted(map(float, input_text[t + 1].split()))
	ken   = sorted(map(float, input_text[t + 2].split()))

	deceit = war = 0
	
	# Deceitful War
	for i in xrange(N):
		if naomi[i] > ken[0]:
			break
	j = 0
	while i < N:
		if naomi[i] > ken[j]:
			deceit += 1
			j += 1
		i += 1

	# War
	high = N - 1
	low = 0
	for block in reversed(naomi):
		if block > ken[high]:
			low += 1
			war += 1
		else:
			high -= 1

	print "Case #" + str((t / 3) + 1) + ":", deceit, war
