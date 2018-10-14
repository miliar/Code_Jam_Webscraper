import sys
import os
import fileinput

if __name__ == '__main__':
	
	lines = []
	line = sys.stdin.readline()
	num = int(line)

	for tc in xrange(num):
		rows, cols = sys.stdin.readline().strip().split()
		rows = int(rows)
		cols = int(cols)

		mat = []
		vals = []
		for x in xrange(rows):
			onerow = [int(y) for y in sys.stdin.readline().strip().split()]
			minr = min(onerow)
			mat.append(onerow)
			for val in onerow:
				vals.append(val)


		svals = [(val, i) for i, val in enumerate(vals)]		
		svals = sorted(svals, key=lambda vv: vv[0])
		#print 'svals', svals

		done = [0 for val in svals]

		sorder = []
		for a,b in svals:
			sorder.append(b)
		#print 'sorder', sorder

		#print 'mat', mat

		matr = map(list, zip(*mat))
		#print 'matr', matr

		finalfound = True
		while 0 in done:	
			#print done		
			mval, mpos = svals[done.index(0)]

			i, j = mpos/cols, mpos%cols
			#print mval, mpos, i, j

			found = True
			for val in mat[i]:
				if val > mval:
					found = False
					break

			#print 'row found', found
			if found:
				for r in xrange(i*cols, i*cols + cols):
					done[sorder.index(r)] = 1
				continue

			found = True
			for val in matr[j]:
				if val>mval:
					found = False
					break

			#print 'col found', found
			if found:
				for r in xrange(0, rows):
					done[sorder.index(r*cols+j)] = 1
				continue

			#print '********'
			sys.stdout.write('Case #{}: NO\n'.format(tc+1))
			#print ''

			finalfound = False
			break

		if finalfound:
			#print '********'
			sys.stdout.write('Case #{}: YES\n'.format(tc+1))
			#print ''














