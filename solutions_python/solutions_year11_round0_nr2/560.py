#!/usr/bin/env python

N = input()

flds = []
base = {}
oposite = {}
res = []

def reset():
	global flds, base, oposite, res
	flds = []
	base = {}
	oposite = {}
	res = []

def getf():
	global flds
	f = flds[0]
	flds = flds[1:]
	return f

def addbase(a,b,c):
	global base
	if a not in base:
		base[a] = {}
	base[a][b] = c

def addoposite(a,b):
	global oposite
	if a not in oposite:
		oposite[a] = []
	oposite[a].append(b)


for n in range(N):
	reset()
	line = raw_input()
	flds = line.strip().split(" ")

	C = int(getf())
	for i in range(C):
		f = getf()
		addbase(f[0],f[1],f[2])
		addbase(f[1],f[0],f[2])
	
	D = int(getf())
	for i in range(D):
		f = getf()
		addoposite(f[0],f[1])
		addoposite(f[1],f[0])

	getf()
	s = getf()
	for i in s:
		res.append(i)
		changed = True
		while changed:
			changed = False
			if (len(res)>1) and (res[-1] in base) and (res[-2] in base[res[-1]]):
				b = base[res[-1]][res[-2]]
				changed = True
				res = res[:len(res)-2]
				res.append(b)
			elif (res[-1] in oposite):
				for o in oposite[res[-1]]:
					if o in res:
						res = []
						break

	print "Case #%d:"%(n+1),
	if len(res)==0: print "[]"
	elif len(res)==1: print "[%s]"%res[0]
	else:
		for i in range(len(res)):
			if (i==0): print "[%s,"%(res[0]),
			elif (i==len(res)-1): print "%s]"%(res[i])
			else: print "%s,"%(res[i]),


