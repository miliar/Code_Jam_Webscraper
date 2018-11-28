#!/usr/bin/python
import re

f_in = open('B-large.in','r')
f_out = open('B-large.out','w')

#f_in = open('in','r')
#f_out = open('out','w')

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char_index = 0

maps = f_in.readline().rsplit()

M = []
res = []
H = 0
W = 0

def trace(r,c):
	global chars
	global char_index
	global M
	global res
	global H
	global W
	r_o = r
	c_o = c
	isSink = False
	while not isSink:
		#print str(r) + '-' + str(c)
		aux = []
		if r > 0: aux.append( (M[r-1][c] , 'N') ) # N
		if c > 0: aux.append( (M[r][c-1] , 'W') ) # W
		if c < W-1: aux.append( (M[r][c+1] , 'E') ) # E
		if r < H-1: aux.append( (M[r+1][c] , 'S') ) # S
		
		aux2 = [ x[0] for x in aux ]
		isSink = (len(filter((lambda x: M[r][c] > x[0]),aux))==0)
		if not isSink:
			#print mine
			mine = aux[aux2.index(min(aux2))][1]
			if mine=='N': r-=1
			if mine=='W': c-=1
			if mine=='E': c+=1
			if mine=='S': r+=1
	if res[r][c]=='':
		res[r][c] = chars[char_index]
		res[r_o][c_o] = chars[char_index]
		char_index+=1
	else:
		res[r_o][c_o] = res[r][c]
	#print res

for m in range(1,1+int(maps[0])):
	aux = f_in.readline().rsplit()
	print aux
	H = int(aux[0])
	W = int(aux[1])
	M = []
	res = []
	char_index = 0
	f_out.write( 'Case #' + str(m) + ':\n' )
	for l in range(0,H):
		a2 = f_in.readline().rsplit()
#		print len(a2)
		M.append( [ int(c) for c in a2 ] )
		res.append([ '' for c in a2 ])
	for r in range(0,H):
		for c in range(0,W):
			if res[r][c]=='': trace(r,c)
	for r in res:
		for c in r:
			f_out.write(str(c) + ' ')
		f_out.write('\n')
