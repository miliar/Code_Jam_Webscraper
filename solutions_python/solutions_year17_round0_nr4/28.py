from sys import stdin
readline = stdin.readline

T = int(readline())

for t in xrange(1, T+1):
	N, M = map(int, readline().strip().split())
	
	inputGrid = [['.' for j in xrange(N)] for i in xrange(N)]
	
	plusgrid = [[0 for j in xrange(N)] for i in xrange(N)]
	plusRuledOut = [[0 for j in xrange(N)] for i in xrange(N)]
	
	crossgrid = [[0 for j in xrange(N)] for i in xrange(N)]
	crossgridRow = [0 for i in xrange(N)]
	crossgridColumn = [0 for j in xrange(N)]
	
	for m in xrange(M):
		model, i, j = readline().strip().split()
		i, j = int(i)-1, int(j)-1
		
		inputGrid[i][j] = model
		if model == '+' or model == 'o':
			plusgrid[i][j] = 1
			for _ in xrange(max(0, i-j), min(N+i-j, N)):
				plusRuledOut[_][_+j-i] = 1
			for _ in xrange(max(0, i+j-(N-1)), min(i+j+1, N)):
				plusRuledOut[_][i+j-_] = 1
		
		if model == 'x' or model == 'o':
			crossgrid[i][j] = 1
			crossgridRow[i] = 1
			crossgridColumn[j] = 1
		
	#Easy stuff: crossgrid - exactly one in every column and row##
	jnext = 0
	for i in xrange(N):
		if crossgridRow[i] == 1:
			continue
		for j in xrange(jnext, N):
			if crossgridColumn[j] == 1:
				continue
			
			crossgrid[i][j] = 1
			crossgridRow[i] = 1
			crossgridColumn[j] = 1
			
			jnext = j+1
			break
	##############################################################
	
	#Smart: Go from the outermost square inwards##################
	squares = [(i, j) for j in xrange(N) for i in xrange(N)]
	squares.sort(key = lambda x: min(x[0], x[1]))
	
	for (i, j) in squares:
		if plusRuledOut[i][j]:
			continue
		else:
			plusgrid[i][j] = 1
			for _ in xrange(max(0, i-j), min(N+i-j, N)):
				plusRuledOut[_][_+j-i] = 1
			for _ in xrange(max(0, i+j-(N-1)), min(i+j+1, N)):
				plusRuledOut[_][i+j-_] = 1
	#############################################################
	
	stylepoints = 0
	changes = []
	for i in xrange(N):
		for j in xrange(N):
			if plusgrid[i][j] == 1 and crossgrid[i][j] == 1:
				stylepoints += 2
				model = 'o'
			elif plusgrid[i][j]	== 1:
				stylepoints += 1
				model = '+'
			elif crossgrid[i][j] == 1:
				stylepoints += 1
				model = 'x'
			else:
				model = '.'
			
			if model != inputGrid[i][j]:
				changes.append('%s %d %d' % (model, i+1, j+1))
	
	print "Case #%d: %d %d" % (t, stylepoints, len(changes))
	for change in changes:
		print change
