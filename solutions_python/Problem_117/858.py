

f = open('land.txt', 'r')

count = int(f.readline().strip())


def check_land(land, N, M):

	max_rows = [max(r) for r in land]
	max_cols = [max([land[n][m] for n in range(N)]) for m in range(M)]

	for i in range(N):
		for j in range(M):
			# check if the field lower than other field in same row
			if land[i][j] < max_rows[i]:
				if land[i][j] < max_cols[j]:
					return "NO"

	return "YES"



for i in range(count):
	land = []
	[N, M] = [int(k) for k in f.readline().strip().split()]
	for j in range(N):
		land.append([int(k) for k in f.readline().strip().split()])
	result = check_land(land, N, M)
	
	print "Case #%d: %s" % (i + 1, result)


