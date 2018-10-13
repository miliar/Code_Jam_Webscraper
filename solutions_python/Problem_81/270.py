#!/usr/bin/python

import sys

def do_case(case, mat, matsize):
	WP = [0 for x in range(matsize)]
	OWP = [0 for x in range(matsize)]
	OOWP = [0 for x in range(matsize)]
	
	for i in range(matsize):
		w=0
		l=0
		owp = []
		for j in range(matsize):
			doowp = True
			if mat[i][j] == '1':
				w += 1
			elif mat[i][j] == '0':
				l += 1
			else:
				doowp = False

			if doowp:
				ow=0
				ol=0
				for k in range(matsize):
					if i == k:
						continue
					if mat[j][k] == '1':
						ow += 1
					elif mat[j][k] == '0':
						ol += 1
				owp.append(float(ow)/(ow+ol))

		WP[i] = float(w)/(w+l)
		OWP[i] = float(sum(owp))/len(owp)
		
	for i in range(matsize):
		t = 0
		sowp = 0.0
		for j in range(matsize):
			if mat[i][j] != '.':
				t += 1
				sowp += OWP[j]
		OOWP[i] = sowp / t

	print 'Case #%d:' % case
	for i in range(matsize):
		print '%.12f' % (0.25*WP[i] + 0.5*OWP[i]+0.25*OOWP[i])


data_lines = sys.stdin.read().splitlines()
data_lines.reverse()
data_lines.pop()

case = 1
while len(data_lines):
	lines = long(data_lines.pop())
	mat = []
	for i in range(lines):
		mat.append(list(data_lines.pop()))
	do_case(case, mat, lines)
	case += 1
