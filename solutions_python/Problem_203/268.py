import sys
if sys.version_info[0]<=2:
	range=xrange
	input=raw_input

def solve0(cake):
	rows=len(cake)
	cols=len(cake[0])
	next=[list(row) for row in cake]
	for r in range(rows):
		row=next[r]
		for c in range(1,cols):
			if row[c]=="?":
				row[c]=row[c-1]
		for c in range(cols-2,-1,-1):
			if row[c]=="?":
				row[c]=row[c+1]
	for c in range(cols):
		for r in range(1,rows):
			if next[r][c]=="?":
				next[r][c]=next[r-1][c]
		for r in range(rows-1,-1,-1):
			if next[r][c]=="?":
				next[r][c]=next[r+1][c]
	return "\n".join(["".join(row) for row in next])

cases=int(input().strip())
for cs in range(1,cases+1):
	rows,cols=map(int,input().strip().split())
	cake=[None]*rows
	for r in range(rows):
		cake[r]=tuple(input().strip())
	print("Case #"+str(cs)+":")
	print(solve0(cake))
