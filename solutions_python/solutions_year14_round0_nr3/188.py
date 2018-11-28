def outer_piece(R,C,sr,sc):
	Grid = ['*'*C + '\n' for x in xrange(sr)] + ['*'*sc + '.'*(C-sc) + '\n' for x in xrange(R-sr)]
	Grid[-1] = Grid[-1][:C-1] + 'c\n'
	return Grid
	
def solve_grid(R, C, M, sr, sc):
	r = R-sr
	c = C-sc

	if M == 0:
		if r == 1 or c == 1:
			return ['Impossible\n']
		else:
			return outer_piece(R,C,sr,sc)	
	
	if r < 1 or c < 1:
		print 'BIG BIG PROBLEMS!'
		return
	
	if r<c and M >= r:
		return solve_grid(R, C, M-r, sr, sc+1)
	elif c<=r and M >= c:
		return solve_grid(R, C, M-c, sr+1, sc)
	else:
		minRC = min(r,c)
		maxRC = max(r,c)
		if minRC <= 2:
			return ['Impossible\n']
		elif maxRC == 3 and M==2:
			return ['Impossible\n']
		else:
			Grid = outer_piece(R,C,sr,sc)
			M1 = min(M, c-2)
			M2 = M-M1
			Grid[sr] = '*'*sc + '*'*M1 + '.'*(c-M1) + '\n'
			for i in xrange(M2):
				Grid[sr+i+1] = Grid[sr+i+1][:sc] + '*' + Grid[sr+i+1][sc+1:]
			return Grid
			
def solve_grid_meta(R, C, M):
	if C==1:
		return ['*\n']*M +['.\n']*(R-M-1) + ['c\n']
	elif R==1:
		return ['*'*M + '.'*(C-M-1) + 'c\n']
	elif M == R*C-1:
		return ['*'*C + '\n']*(R-1) + ['*'*(C-1)+'c\n']
	elif M == 0:
		return ['.'*(C-1)+'c\n'] + ['.'*C + '\n']*(R-1)
	else:
		return solve_grid(R,C,M,0,0)


def solve(in_name, out_name):
	fin = open(in_name, 'r');
	L = [map(int, x.strip().split()) for x in fin.readlines()]
	fin.close()
	
	fout = open(out_name, 'w')
	for i in xrange(1, len(L)):
		fout.writelines(['Case #' + str(i) + ':\n'])
		fout.writelines(solve_grid_meta(L[i][0], L[i][1], L[i][2]))
	fout.close()
	
	return

#sys.setrecursionlimit(1000)	
#solve('C-small-attempt3.in', 'C-small-attempt3.out')
solve('C-large.in', 'C-large.out')

#solve('C-test.in', 'C-test.out')
