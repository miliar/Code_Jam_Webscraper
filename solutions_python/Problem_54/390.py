import sys, os, string, re

line = sys.stdin.readline()
C = int(line)

for case_num in range(1, C+1):
	line = sys.stdin.readline()
	parts = line.split()
	N = int(parts[0])
	ts = []
	for i in range(N):
		ts.append(int(parts[1+i]))
	
	ts.sort()
	best_factor = 1
	best_increment = 0

	for i in range(1, len(ts)):
		d = ts[i]-ts[i-1]

	sys.stdout.write('Case #%d: %d\n' % (case_num, best_increment)
