#!/usr/bin/env python2.7

from sys import stdin

def getLineStatus(symbols):
	symbols = ''.join(symbols)
	symbols = symbols.replace('T', '')
	if symbols in ('XXX', 'XXXX'): return 'X'
	elif symbols in ('OOO', 'OOOO'): return 'O'
	else: return

def getStatus(lines):
	# print lines
	
	for line in lines:
		lineStatus = getLineStatus(line)
		if lineStatus: return '%s won' % lineStatus

	for j in xrange(4):
		lineStatus = getLineStatus(map(lambda line: line[j], lines))
		if lineStatus: return '%s won' % lineStatus

	for line in (lines[0][0],lines[1][1],lines[2][2],lines[3][3]), (lines[0][3],lines[1][2],lines[2][1],lines[3][0]):
		lineStatus = getLineStatus(line)
		if lineStatus: return '%s won' % lineStatus

	if ''.join(lines).find('.') != -1: return 'Game has not completed'
	else: return 'Draw'

numcases = int(stdin.readline().strip())
for casenum in xrange(numcases):
	lines = []
	for i in xrange(4): line = stdin.readline()[:4]; lines.append(line)
	print "Case #%d: %s" % (casenum+1, getStatus(lines))
	line = stdin.readline()