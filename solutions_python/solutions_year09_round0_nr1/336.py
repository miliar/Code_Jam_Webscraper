#!/usr/bin/env python

import sys

tree = {}

def parseEntry(entry):
	state = 0
	ret = []
	tmp = []
	for c in entry:
		if c == '(':
			state = 1
			tmp = []
		elif c == ')':
			state = 0
			ret.append(tmp)
		else:
			if state == 0:
				ret.append([c])
			else:
				tmp.append(c)
	return ret

def addToTree(word):
	global tree
	tmp = tree
	for c in word:
		if not c in tmp:
			tmp[c] = {}
			tmp = tmp[c]
		else:
			tmp = tmp[c]

def entryInTree(entry):
	global tree
	return recEntryInTree(parseEntry(entry), tree)

def recEntryInTree(entryArr, treeL):
	if len(entryArr) == 0:
		return 1
	ret = 0
	for let in entryArr[0]:
		if not let in treeL:
			continue
		ret = ret + recEntryInTree(entryArr[1:], treeL[let])
	return ret

def parseFile(fname):
	lines = open(fname).read().split('\n')
	data = lines[0].split(' ')
	wordcount = int(data[1])
	tests = int(data[2])
	lines = lines[1:]
	for i in range(wordcount):
		addToTree(lines[i].strip())
	lines = lines[wordcount:]
	for i in range(1, tests + 1):
		print 'Case #%d: %d' % (i, entryInTree(lines[i-1].strip()))

if __name__ == '__main__':
	parseFile(sys.argv[1])

