#!/usr/bin/env python
import math
import sys
import os
from os import system

def calculate(tiles,R,C):
	rowstate = 0
	colstate = []
	for k in range(C):
		colstate.append(0)
	for j in range(R):
		rowstate = 0
		for k in range(C):
			if tiles[j][k] is ".":
				if rowstate is 1:
					print rowstate,colstate,j,k,tiles
					return "Impossible"
				if colstate[k] is 1:
					print rowstate,colstate,j,k,tiles
					return "Impossible"
				if colstate[k] is 2:
					print rowstate,colstate,j,k,tiles
					return "Impossible"
				rowstate = 0
				colstate[k] = 0
			if tiles[j][k] is "#":
				if j is 0:
					if rowstate is 0:
						tiles[j][k] = "/"
						rowstate = 1
						colstate[k] = 1
					elif rowstate is 1:
						tiles[j][k] = "\\"
						rowstate = 2
						colstate[k] = 2
					elif rowstate is 2:
						tiles[j][k] = "/"
						rowstate = 1
						colstate[k] = 1
				elif j > 0 and rowstate is 0:
					if colstate[k] is 0:
						tiles[j][k] = "/"
						colstate[k] = 1
						rowstate = 1
					elif colstate[k] is 1:
						tiles[j][k] = "\\"
						colstate[k] = 3
						rowstate = 1
					elif colstate[k] is 2:
						print rowstate,colstate,j,k,tiles
						return "Impossible"
					elif colstate[k] is 3:
						tiles[j][k] = "/"
						colstate[k] = 1
						rowstate = 1
				elif j > 0 and rowstate is 1:
					if colstate[k] is 0:
						tiles[j][k] = "\\"
						colstate[k] = 1
						rowstate = 2
					elif colstate[k] is 1:
						tiles[j][k] = "/"
						colstate[k] = 3
						rowstate = 2
					elif colstate[k] is 2:
						tiles[j][k] = "/"
						colstate[k] = 3
						rowstate = 2
					elif colstate[k] is 3:
						tiles[j][k] = "\\"
						colstate[k] = 1
						rowstate = 2
				elif j > 0 and rowstate is 2:
					if colstate[k] is 0:
						tiles[j][k] = "/"
						colstate[k] = 1
						rowstate = 1
					elif colstate[k] is 1:
						tiles[j][k] = "\\"
						colstate[k] = 3
						rowstate = 1
					elif colstate[k] is 2:
						print rowstate,colstate,j,k,tiles
						return "Impossible"
					elif colstate[k] is 3:
						tiles[j][k] = "/"
						colstate[k] = 1
						rowstate = 1
				print "***",j,k,rowstate,colstate
	return tiles



fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	ret = ""
	l = fp.readline().split()
	R = int(l[0])
	C = int(l[1])
	tiles = []
	statenum = []
	for k in range(C):
		statenum.append(0)
	for j in range(R):
		rownumber = 0
		tiles.append([])
		tokens = fp.readline()
		for k in range(C):
			tiles[j].append(tokens[k])
			if tokens[k] is "#":
				rownumber += 1
				statenum[k] += 1
		if rownumber%2 is 1:
			ret = "Impossible"
	
	
	print tiles
	for k in range(C):
		if statenum[k]%2 is 1:
			ret = "Impossible"
	if ret is "":
		ret = calculate(tiles,R,C)

	fout.write('Case #%d:\n'%((i+1)))
	if ret is "Impossible":
		fout.write("%s\n"%(ret))
	else :
		for j in range(R):
			for k in range(C):
				fout.write('%s'%(ret[j][k]))
			fout.write('\n')
