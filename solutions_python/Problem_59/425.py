#! /usr/bin/python
import os
import sys

def AddDir(dirTree, dir, level):
	if FindInList(dirTree[level], dir) == 0:
		dirTree[level].append(dir)
	return dirTree

def FindInList(list, ele):
	for item in list:
		if ele == item:
			return 1
	return 0

if len(sys.argv) != 2:
	print 'USAGE: q1.py input.in'
	sys.exit()

fIn = open(sys.argv[1], 'r')
param = fIn.readline().split()
T = int(param[0])
for i in range(T):
	dirTree = [[] for row in range(100)]
	line = fIn.readline()
	N = int(line.split()[0])
	M = int(line.split()[1])
	for n in range(N):
		line = fIn.readline().split('/')
		line[-1] = line[-1][0:-1]
		line.pop(0)
	#	print line
		level = 0
		for d in range(len(line)):
			dir = line[0]
			for dd in range(d):
				dir = dir + '_' + line[dd+1]
	#		print dir
			dirTree = AddDir(dirTree, dir, level)
			level += 1
	
#	print dirTree
	mkdir = 0
	for m in range(M):
		line = fIn.readline().split('/')
		line[-1] = line[-1][0:-1]
		line.pop(0)
		level = 0
		for d in range(len(line)):
			dir = line[0]
			for dd in range(d):
				dir = dir + '_' + line[dd+1]
			if FindInList(dirTree[level], dir) == 0:
				mkdir += 1
				AddDir(dirTree, dir, level)
			level += 1
#	print dirTree	
	print 'Case #'+str(i+1)+': '+str(mkdir)
#		print 'Case #'+str(i+1)+': OFF'

