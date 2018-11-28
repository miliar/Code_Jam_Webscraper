import sys, os

inf = open(sys.argv[1] , 'r')
outf = open('A-out', 'w')

cast_cnt = int(inf.readline())

def count_blue (grids):
	count = 0
	for gr in grids:
		for g in gr:
			if g == '#':
				count += 1
	return count

def is_four_times (grids):
	i = count_blue(grids)
	return (i % 4) == 0

def try_replace (grids):
	for i in range(len(grids)):
		for j in range(len(grids[i])):
			if grids[i][j] == '#':
				# Try to replace
				if j == (len(grids[i]) - 1):
					return False
				if i == (len(grids) - 1):
					return False

				if grids[i][j + 1] == '#' and grids[i + 1][j] == '#' and grids[i + 1][j + 1] == '#': # Top Two is Blue
					grids[i][j + 1] = '\\'
					grids[i][j] = '/'
					grids[i + 1][j] = '\\'
					grids[i + 1][j + 1] = '/'
				else:
					return False
					
	return grids

for i in range(cast_cnt):
	ele = inf.readline().split()
	row_cnt = int(ele[0])
	column_cnt = int(ele[1])
	grids = []
	for j in range(row_cnt):
		l = []
		el = inf.readline()
		for k in range(column_cnt):
			l.append(el[k])
		grids.append(l)
	
	if not is_four_times(grids):
		outf.write('Case #%d:\nImpossible\n'% (i + 1,))
		continue
	
	ret = try_replace(grids)
	if ret == False:
		outf.write('Case #%d:\nImpossible\n'% (i + 1,))
	else:
		outf.write('Case #%d:\n' % (i+1,))
		for g in ret:
			for gi in g:
				outf.write('%s' % (gi,))
			outf.write('\n')

inf.close()
outf.close()
