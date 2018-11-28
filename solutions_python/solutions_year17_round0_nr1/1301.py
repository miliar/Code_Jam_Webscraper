import sys
import math

sys.stdout = open('out', 'w')
with open(sys.argv[1], 'r') as f:
	l = f.readline().split(' ')
	for p in range(int(l[0])):
		l = f.readline().split(' ')
		k = int(l[1])
		s = list(l[0])
		num = 0
		for i in range(len(s)-k+1):
			if s[i] == '-':
				for j in range(k):
					if s[i+j] == '-':
						s[i+j] = '+'
					else:
						s[i+j] = '-'
				num += 1
		fail = False
		for i in range(k-1):
			if s[i+len(s)-k+1] == '-':
				fail = True

		if fail == True:
			print "Case #" + str(p + 1) + ":", "IMPOSSIBLE"
		else:
			print "Case #" + str(p + 1) + ":", num

