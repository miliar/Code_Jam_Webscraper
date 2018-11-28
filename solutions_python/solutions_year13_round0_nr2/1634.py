def case(n):
	N, M = map(int, raw_input().split(' '))
	
	pattern = [[[v, False] for v in map(int, raw_input().split(' '))] for _ in xrange(N)]
	lowest = 100
	
	for y in xrange(N):
		for x in xrange(M):
			if pattern[y][x][0] < lowest:
				lowest = pattern[y][x][0]
	
	low_points = []
	
	for y in xrange(N):
		for x in xrange(M):
			if pattern[y][x][0] == lowest:
				low_points.append((x, y))
	
	possible = True
	
	for point in low_points:
		pat_ref = pattern[point[1]][point[0]]
		
		val = pat_ref[0]
		
		horz = True
		vert = True
		
		for y in xrange(N):
			p = pattern[y][point[0]]
			p[1] = True
			vert = vert and (p[0] == val)
		
		for x in xrange(M):
			p = pattern[point[1]][x]
			p[1] = True
			horz = horz and (p[0] == val)
		
		possible = possible and (horz or vert)
	
	print 'Case #%d: %s' % (n, ['NO', 'YES'][int(possible)])

if __name__ == '__main__':
	for i in xrange(int(raw_input())):
		case(i + 1)