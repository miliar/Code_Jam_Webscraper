# /usr/bin/python
import sys

def dbg(s): sys.stderr.write(str(s) +"\n")
def reads(t): return list(map(t, input().split(" ")))
def read(t) : return t(input())



T = read(int)

for t in range(1, T+1):
	[N, M] = reads(int)
	row_max = [0] * N
	col_max = [0] * M
	
	G = []
	possible = True
	
	for i in range(0, N):
		row = reads(int)
		G.append(row)
		rm = 0;
		
		if possible:
			for j in range(0,M):
				h = row[j]
				rm = max(h, rm)
				col_max[j] = max(h, col_max[j])
				if h < col_max[j] and h < rm:
					possible = False
					break

		row_max[i] = rm

	for i in range(0, N):
		if possible:
			for j in range(0, M):
				h = G[i][j]
				if h < col_max[j] and h < row_max[i]:
					possible = False
					break
		else:
			break

	if possible:
		p = "YES"
	else:
		p = "NO"	
		
	print("Case #%d: %s" % (t, p))
