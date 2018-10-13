#!/usr/bin/python
# -*- coding: utf-8 -*-



nextName = (i for i in 'abcdefghijklmnopqrstuvwxyz')

def calc(m, size):
	print(m)

	ans = []
	for r in range(size[0]):
		col = []
		for c in range(size[1]):
			col.append('')
		ans.append(col)

	for r in range(size[0]):
		for c in range(size[1]):
			follow(r, c, m, ans, size)

	return ans

def follow(r, c, m, ans, size):
	if ans[r][c]:
		return ans[r][c]

	#calc lowest neighbor
	min = m[r][c]
	nr = r
	nc = c
	if not (r+1 >= size[0]):
		if m[r+1][c] <= min:
			min = m[r+1][c]
			nr =r+1
			nc = c
	if not (c+1 >= size[1]):
		if m[r][c+1] <= min:
			min = m[r][c+1]
			nr = r
			nc = c+1
	if not (c-1 < 0):
		if m[r][c-1] <= min:
			min = m[r][c-1]
			nr = r
			nc = c-1
	if not (r-1 < 0):
		if m[r-1][c] <= min:
			min = m[r-1][c]
			nr = r-1
			nc = c

	if min == m[r][c]:
		char = nextName.next()
		ans[r][c] = char
		print("setting {0} {1} to {2}".format(r, c, char))
		return char

	print("recusing")
	char = follow(nr, nc, m, ans, size)
	ans[r][c] = char
	print("setting after recurse {0} {1} to {2}".format(r, c, char))
	return char

def read(fin, fout):
	line = fin.next()
	cases = int(line)

	case = 1
	for line in fin:
		global nextName
		nextName = (i for i in 'abcdefghijklmnopqrstuvwxyz')

		size = [int(i) for i in line.split(' ')]

		m = []
		for i in range(size[0]):
			line = fin.next()
			m.append([int(j) for j in line.split(' ')])

		ans = calc(m, size)

		fout.write("Case #{0}:\n".format(case))
		for row in ans:
			for char in row:
				fout.write("{0} ".format(char))
			fout.write("\n")

		case += 1

if __name__=="__main__":
	import sys
	fin = file(sys.argv[1])
	fout = file(sys.argv[2], 'w')
	read(fin, fout)
	fin.close()
	fout.close()
