import sys
import copy

def solve(mat, n, m):
	for i in range(0,n):
		for j in range(0,m):
			if not checkCell(mat,n,m,i,j):
				return "NO"
				
	return "YES"
	
def checkCell(mat, n, m, l, c):
	vert = True
	for i in range(0,n):
		if mat[i][c] > mat[l][c]:
			vert = False

	horiz = True
	for j in range(0,m):
		if mat[l][j] > mat[l][c]:
			horiz = False
		
	return vert or horiz


f = open(sys.argv[1])
o = open("p2.out","w")
with f:
	with o:
		t = int(f.readline())
		for k in range(0,t):
			line = f.readline().strip()
			n,m = map(lambda p:int(p), line.split(" "))
			mat = []
			for i in range(0,n):
				mat.append([])
				line = f.readline().strip()
				map(lambda p: mat[i].append(int(p)), line.split(" "))
			result = solve(mat, n, m)
			o.write("Case #%d: %s\n" % (k+1, result))
