#!/usr/bin/python

import re

filename = "B-large"
input_filename = filename + ".in"
output_filename = filename + ".out"

def zeros(H, W):
	out = []
	row = []
	for i in range(W):
		row.append(0)
	for i in range(H):
		newrow = list(row)
		out.append(newrow)
	return out

def substitute(map, H, W, pattern, repl):
	for i in range(H):
		for j in range(W):
			if map[i][j] == pattern:
				map[i][j] = repl
	return map

def do_basins(map, H, W):
	sink = zeros(H, W)
	x = 0
	y = 0
	mark = 1
	movs = [(-1,0), (0,-1), (0,1), (1,0)]

	while ( x < H and y < W ):
		px = x
		py = y
		while (True):
			sink[px][py] = mark
			minval = map[px][py]
			optmove = (0, 0)
			for pair in movs:
				newpx = px + pair[0]
				newpy = py + pair[1]
				if ( newpx >= 0 and newpx < H and newpy >=0 and newpy < W):
					if map[newpx][newpy] < minval:
						minval = map[newpx][newpy]
						optmove = pair
			if (optmove == (0, 0)):
				break
			newpx = px + optmove[0]
			newpy = py + optmove[1]
			if sink[newpx][newpy] == 0:
				sink[newpx][newpy] == mark
				px = newpx
				py = newpy
			else:
				sink = substitute(sink, H, W, mark, sink[newpx][newpy])
				break
		mark += 1
		while (sink[x][y]!=0):
			if y < W-1:
				y += 1
				continue
			if x == H-1:
				return sink
			if y == W-1:
				y = 0
				x += 1
				continue
	return sink

def main():
	fi = open(input_filename,"r")
	fo = open(output_filename,"w")
	list = "abcdefghijklmnopqrstuvwxyz"

	T = int(fi.readline())
	for case in range(T):
		l = fi.readline().split()
		(H, W) = (int(l[0]), int(l[1]))
		map = []
		for i in range(H):
			row = []
			for val in fi.readline().split():
				row.append(int(val))
			map.append(row)
		out = do_basins(map, H, W)
		count = 0
		mapping = {}
		fo.write("Case #" + str(case+1) + ": " + "\n")
		for i in range(H):
			for j in range(W):
				if mapping.has_key(out[i][j]):
					pass
				else:
					mapping[out[i][j]] = list[count]
					count += 1
				fo.write(mapping[out[i][j]] + " ")
			fo.write("\n")

if __name__ == "__main__":
	main()
