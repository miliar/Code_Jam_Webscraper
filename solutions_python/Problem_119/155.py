#!/usr/bin/python
import sys


def add(keys, arr):
	for k in arr:
		if k in keys:
			keys[k] += 1
		else:
			keys[k] = 1

def remove(keys, arr):
	for k in arr:
#		if keys[k]==1:
#			del keys[k] 
#		else:
		keys[k] -= 1


def run(keys, chestsOpen):
	KEY = "keys="+str(keys)+";open="+str(chestsOpen)
#	print "RUN: ",keys, chestsOpen
	if KEY in vis:
		return None

	if len(chestsOpen)==0:
		return []

	n = len(chestsOpen)
	for i in range(n):
		chest = chestsOpen[i];
		needKey = chests[chest]
		if needKey in keys and keys[needKey]>0:
			# Open it
			del chestsOpen[i]
#			if keys[needKey]==1:
#				del keys[needKey]
#			else:
			keys[needKey] -= 1

			add(keys, contents[chest])
			res = run(keys, chestsOpen)
			if res!=None:
				res.append(chest)
				return res
			remove(keys, contents[chest])

			# Rollback
#			if needKey in keys:
			keys[needKey] += 1
#			else:
#				keys[needKey] = 1
			chestsOpen.insert(i, chest)

	vis[KEY] = True
	return None



contents = []
vis = {}
chests = []
N = -1

inp = [map(int,line.split()) for line in sys.stdin]
T = inp[0][0]
line = 1
for t in range(T):
	(startKeys,N) = (inp[line][0], inp[line][1])
	line += 1
	haveKeys = inp[line]
	line += 1
	chests = []
	contents = []
	for ch in range(N):
	#	print ch
		chests.append(inp[line][0])
		contents.append(inp[line][2:])
		line += 1

	myKeys = {}
	for k in haveKeys:
		if k in myKeys:
			myKeys[k] += 1
		else:
			myKeys[k] = 1

	chestsOpen = range(N)

#	print "startKeys",startKeys, "N",N, "keys=",haveKeys, "chests open with ",chests, "contents=",contents

	vis = {}
	result = run(myKeys, chestsOpen)
	if result is not None:
#		print "RESULT "+str(result)
		s = " ".join(map(lambda n: str(n+1),result[::-1]))
	else:
		s = "IMPOSSIBLE"
	print "Case #%d: %s" % (t+1, s)

