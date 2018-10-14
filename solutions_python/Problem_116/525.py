import sys

def solve(mat):
	for sym in ["X", "O"]:
		won = checkEqual(mat, sym, 0, 0, 1, 0) or checkEqual(mat, sym, 0, 0, 0, 1) \
		or checkEqual(mat, sym, 0, 1, 1, 0) or checkEqual(mat, sym, 1, 0, 0, 1) \
		or checkEqual(mat, sym, 0, 2, 1, 0) or checkEqual(mat, sym, 2, 0, 0, 1) \
		or checkEqual(mat, sym, 0, 3, 1, 0) or checkEqual(mat, sym, 3, 0, 0, 1) \
		or checkEqual(mat, sym, 0, 0, 1, 1) or checkEqual(mat, sym, 0, 3, 1, -1)
		if won:
			return "%s won" % sym
	for i in range(0,4):
		for j in range(0,4):
			if mat[i][j] == ".":
				return "Game has not completed"
	return "Draw"
			
def checkEqual(mat, symbol, x0, y0, px, py):
	x = x0
	y = y0
	for i in range(0,4):
		if mat[x][y] != symbol and mat[x][y] != "T":
			return False
		x += px
		y += py
	return True
	
f = open(sys.argv[1])
o = open("p1.out","w")
with f:
	with o:
		n = int(f.readline())
		for i in range(0,n):
			mat = []
			for j in range(0,4):
				mat.append([])
				line = f.readline().strip()
				for k in line:
					mat[j].append(k)
			result = solve(mat)
			o.write("Case #%d: %s\n" % (i+1, result))
			f.readline()
