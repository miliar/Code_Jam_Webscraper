#!/usr/bin/python

def harm(a,b):
	return (max(a,b)%min(a,b)==0)

def next_correct(mine, his, m):
	if (mine>=his):
		return his*((mine/his)+1)
		return his + mine - mine%his
	else:
		for x in range(mine+1, min(m,his)+1):
			if his%x==0:
				return x
	return m+1

#for a in [(5,15),(6,15),(15,5),(16,6)]:
#	print a, next_correct(a[0],a[1],100)

CASES = input()
for tcase in range(1,CASES+1):
	print "Case #%d:"%tcase,
	N = input()
	L = input()
	H = input()
	others = []
	for i in range(N):
		hz = input()
		others.append((hz,hz))
	#print L,H,N, others

	finished = False
	mine = L
	ok = False
	for mine in range(L,H+1):
		if ok: break
		c = 0
		for o in others:
			if harm(mine,o[1]):
				c = c+1
			else:
				break
		if not ok and c==len(others):
			print mine
			ok = True
	if not ok: print "NO"
#	while not finished and mine<=H:
#		finished = True
#		for i in range(N):
#			o = others[i]
#	#		print "harm %s %s == "%(mine,o)
#	#		print harm(mine,o[0])
#			if not harm(mine,o[0]):
#				mine = next_correct(mine, o[1], H)
#				others[i] = (mine, o[1])
#				finished = False
#	if (mine>H):
#		print "NO"
#	else:
#		print mine
				



