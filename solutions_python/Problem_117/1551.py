import sys
from sets import Set


def solve(D, H, rows, cols):	
	for h in H:
		# Check rows
		for r in range(0,rows):
			count = 0
			for c in range(0,cols):
				if D[r][c] == h or D[r][c] == -1:
					count += 1
			if count == 0 or count == cols:
				for c in range(0,cols):
					if D[r][c] == h or D[r][c] == -1:
						D[r][c] = -1

		# Check cols
		for c in range(0,cols):
			count = 0
			for r in range(0,rows):
				if D[r][c] == h or D[r][c] == -1:
					count += 1
			if count == 0 or count == rows:
				for r in range(0,rows):
					if D[r][c] == h or D[r][c] == -1:
						D[r][c] = -1
				
		for r in range(0,rows):
			for c in range(0,cols):
				if D[r][c] == h:
					return "NO"

	return "YES"


cases = sys.stdin.readline()

for case in range(0,int(cases)):	
	H = Set()
	D = []

	# Read
	N,M = [int(v) for v in sys.stdin.readline().split()]
	for y in range(0,N):
		line = [int(v) for v in sys.stdin.readline().split()]
		D.append(line)
		for v in line:
			H.add(v)
	
	print "Case #%d: %s" % (case+1, solve(D, H, N, M))
