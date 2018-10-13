#!/usr/bin/env python2.7

def solve(filename):
	i = open(filename, "Ur")
	out = open("out1", "w")
	l = i.readlines()
	num = int(l[0])
	for y in range(num):
		grid = l[1 + 5 * y : 5 * (1 + y)]
		p = 0
		o = 0
		for x in range(4):
			ver = high(grid, x)
			p += scheck(grid[x], "X") + scheck(ver, "X")
			o += scheck(grid[x], "O") + scheck(ver, "O")
		for x in dia(grid):
			p += scheck(x, "X")
			o += scheck(x, "O")
		if o > p:
			out.write("Case #" + str(y + 1) + ": O won\n")
		elif p > o:
			out.write("Case #" + str(y + 1) + ": X won\n")
		elif full(grid) or p == o != 0:
			out.write("Case #" + str(y + 1) + ": Draw\n")
		else:
			out.write("Case #" + str(y + 1) + ": Game has not completed\n")

def high(grid, num):
	o = ""	
	for x in range(4):
		o += grid[x][num]
	return o	

def dia(grid):
	o = ["", ""]
	for x in range(4):
		o[0] += grid[x][x]
		o[1] += grid[x][3-x]
	return o

def full(string):
	for x in string:
		for y in x:
			if y == ".": return False
	return True

def scheck(string, letter):
	string = string.strip()	
	for x in string:
		if x != letter and x != "T":
			return 0
	return 1	

solve("in1")
