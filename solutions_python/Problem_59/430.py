#!/usr/bin/python
import sys
import re

_dprint = False
answer = 0

filesys = []

def mkdir(f):
	count = 0
	c = re.split('/',f)
	if _dprint: print c
	path=""
	for i in c:
		path += '/'+i
		if path not in filesys:
			if _dprint: print "Adding dir:",path
			filesys.append(path)
			count += 1
	return count


def _output(case, answer):
	print "Case #{0}: {1}".format(case, answer)

# get number of cases
infile = open(sys.argv[1],'r')
cases = int(infile.readline())
if _dprint: print cases

for case in range(1,1+cases):
	if _dprint: print "******** Starting Case:",case
	filesys = []
	(N, M) = map(int,re.findall(r'\w+',infile.readline()))
	if _dprint: print N, M
	for exist in range(N):
		inp2 = infile.readline().rstrip('\n')
		if _dprint: print "got directory:", inp2,":"
		mkdir(inp2[1:])

	if _dprint: print "filesystem:", filesys

	answer = 0
	for need in range(M):
		inp2 = infile.readline().rstrip('\n')
		if _dprint: print "need directory:", inp2,":"
		answer += mkdir(inp2[1:])
	_output(case,answer)
infile.close()
