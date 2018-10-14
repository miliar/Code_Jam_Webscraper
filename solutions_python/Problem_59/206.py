#!/usr/bin/python2.6
import sys
data = sys.stdin
caseno = int(data.readline())
for case in xrange(1,caseno+1):
	print "Case #%d:"%case,
	N,M = map(int,data.readline().split())
	curd = {} 
	for dir in xrange(N):
		path = data.readline().strip().split('/')[1:]
		uri = ''
		for d in path:
			uri += '/'+d
			curd[uri]=''

	creatd = [] 
	for dir in xrange(M):
		path = data.readline().strip().split('/')[1:]
		creatd.append(path)
	C = 0
	for uri in creatd:
		pth = ''
		C += len(uri)
		for dir in uri:
			pth += '/'+dir
			if curd.has_key(pth):
				C = C-1
			curd[pth]=''

	print C
