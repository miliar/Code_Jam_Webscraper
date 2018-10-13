fin = open('a2.txt')
fout = open('out.txt', 'w')

cases = int(fin.readline())

def check(board, si, sj, n, m):
    z = board[si][sj]
    p1, p2, p3, p4 = True, True, True, True

    if si > 0:
	for i in xrange(0, si):
	    if board[i][sj] > z:
		p1 = False
		break
	    
    if si < (n - 1):
	for i in xrange(si + 1, n):
	    if board[i][sj] > z:
		p2 = False
		break

    if p1 and p2:
	return True

    if sj > 0:
	for j in xrange(0, sj):
	    if board[si][j] > z:
		p3 = False
		break
    if sj < (m - 1):
	for j in xrange(sj + 1, m):
	    if board[si][j] > z:
		p4 = False
		break
    if (p3 and p4):
	return True
    return False


for case in xrange(0, cases):
    n, m = (int(x) for x in fin.readline().rstrip().split())
    board = []
    for i in xrange(0, n):
	board.append([int(x) for x in fin.readline().rstrip().split()])

    if n == 1 or m == 1:
	fout.write("Case #{}: YES\n".format(case + 1))
	continue
    passed = True
    for i in xrange(0, n):
	for j in xrange(0, m):
	    if not check(board, i, j, n, m):
		passed = False
		break
	if not passed:
	    break

    for b in board:
	print b

    print passed
    if passed:
	fout.write("Case #{}: YES\n".format(case + 1))
    else:
	fout.write("Case #{}: NO\n".format(case + 1))

	    
