import sys
#import math
#import 

file = open(sys.argv[1])
out = open('out.txt', 'w')

total_cases = int(file.readline())

case = 1

while case <= total_cases:
	N = int(file.readline())
	n = 0
	matrix = []
	W = []
	L = []
	while n < N:
		line = file.readline().replace('\n', '')
		matrix.append(line)
#		print n, line
		temp = line.replace('.', '')
		W.append(len(temp.replace('0', '')))
		L.append(len(temp.replace('1', '')))
		n += 1
#	print W
#	print L
#	print matrix

	OWP = []

	w = 0
	l = 0
	for i in range(N):
#		print 'OWP for ', i
		owp = 0
		count = 0
		for j in range(N):
			if j != i:
				temp = matrix[j]
				if temp[i] == '.':
					continue
#				print i, j, matrix[j]
				w = 0
				l = 0
				for k in range(N):
					if k != i and k != j:
						if temp[k] == '1':
							w += 1
						elif temp[k] == '0':
							l += 1
#				print 'w, l, owp ', w, l, owp
				count += 1
				if w + l > 0:
					owp += float(w)/(w+l)
#		print 'owp, count = ', owp, count
		OWP.append(owp/count)
#	print OWP

	res = 'Case #' + str(case) + ':\n'
#	print res
	out.write(res)

	for i in range(N):
		sol = 0
		games = W[i] + L[i]
		if games > 0:
			sol = 0.25 * W[i] / games + 0.5 * OWP[i]
			oowp = 0
			count = 0
			for j in range(N):
				if i != j and matrix[j][i] != '.':
					oowp += OWP[j]
					count += 1
			if count > 0:
				sol += 0.25 * oowp / count
		out.write(str(sol) + '\n')
	case += 1
