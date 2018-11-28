def laneIsOnes(lane):
	yes = True
	for c in lane:
		yes &= (c == 1)
	return yes

f = open(raw_input())
T = int(f.readline())

for t in xrange(T):
	R, C = [int(x) for x in f.readline().strip().split()]
	board = [[int(x) for x in f.readline().strip().split()] for r in xrange(R)]

	possible = True
	for r in xrange(R):
		for c in xrange(C):
			if board[r][c] == 1:
				possible &= (laneIsOnes(board[r]) or laneIsOnes([board[x][c] for x in xrange(R)]))

	print "Case #%d: %s" % (t+1, "YES" if possible else "NO")

"""
if a_ij is the smallest number, then all of row i and col j must be a_ij
what about second smallest, etc?
1 2 3
1 2 3
1 1 1
mow(col 3, 3)
mow(col 2, 2)
mow(col 1, 1)
mow(row 1, 1)

2 1 2
1 1 1
2 1 2

1 1 1
1 2 1
1 1 1

However,
1 2 3
1 3 3
1 1 1
is NOT POSSIBLE. why?
if col j is mowed with height h, then a_ij <= h for all i
if row i is mowed with height h, then a_ij <= h for all j
"""

f.close()