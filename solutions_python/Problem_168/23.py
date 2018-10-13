import math
import re

def solve(r,c,grid):
	i = 0
	for m in range(r):
		for n in range(c):
			if grid[m][n]!=".":
				impossible = 1
				off = 1
				for j in range(0,m):
					if grid[j][n]!=".":
						impossible = 0
						off = 0
				i += (grid[m][n]=="^")*off
				off = 1
				for j in range(m+1,r):
					if grid[j][n]!=".":
						impossible = 0
						off = 0
				i += (grid[m][n]=="v")*off
				off = 1
				for j in range(0,n):
					if grid[m][j]!=".":
						impossible = 0
						off = 0
				i += (grid[m][n]=="<")*off
				off = 1
				for j in range(n+1,c):
					if grid[m][j]!=".":
						impossible = 0
						off = 0
				i += (grid[m][n]==">")*off
				if impossible == 1 :
					return "IMPOSSIBLE"
	return i

inp = open("A-large.in","r")
out = open("A-large","w")
lines = inp.readlines()
i=1
count=1
while i<len(lines):
	[r,c] = [int(x) for x in re.split(" ",lines[i])]
	grid = [lines[i+j][0:c] for j in range(1,r+1)]
	out.write("Case #"+str(count)+": "+"{:}".format(solve(r,c,grid))+"\n")
	i+=(r+1)
	count+=1
out.close()
inp.close()

