def solve():

	[N, M] = [int(X) for X in infile.readline().split()]

	lawn = []
	rows = [10] * N
	cols = [10] * M

	for x in range(N):
		lawn.append([int(X) for X in infile.readline().split()])
		rows[x] = max(lawn[x])

	for y in range(M):
		cols[y] = max([X[y] for X in lawn])

	for x in range(N):
		for y in range(M):
			field = lawn[x][y]
			if field != rows[x] and field != cols[y]:
				return "NO"
	return "YES"

infile = open('B-large.in', 'r')
outfile = open('large.out', 'w')

T = int(infile.readline())

for t in range(T):
	outfile.write("Case #" + str(t+1) + ": " + solve() + "\n")
