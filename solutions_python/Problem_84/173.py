#!/usr/bin/python
def count(c, sl):
	res = 0
	for s in sl:
		for i in s:
			if i==c:
				res += 1
	return res

def getPos(s):
	res = []
	for i in range(len(s)-1):
		if (i-1 not in res) and (s[i] == "#") and (s[i+1] == "#"):
			res.append(i)
	return res

T = int(raw_input())
for t in range(T):
	R,C = [int(i) for i in raw_input().split()]
	lines = []
	for r in range(R):
		lines.append(list(raw_input()))
	
	print "Case #%d:" % (t+1)
	if (count("#", lines) % 4) != 0:
		print "Impossible"
		continue
	"""
	for l in lines:
		print "".join(l)
	print "==============="
	"""
	for r in range(R-1):
		l1 = lines[r]
		l2 = lines[r+1]
		pos1 = getPos(l1)
		pos2 = getPos(l2)
		for p in pos1:
			if p in pos2:
				lines[r][p:p+2] = ["/","\\"]
				lines[r+1][p:p+2] = ["\\","/"]
	flag = True	
	for l in lines:
		if "#" in l:
			flag = False
			break
	if not flag: 
		print "Impossible"
		continue
	
	for l in lines:
		print "".join(l)
		