#!/bin/python

tests=int(raw_input())

for t in range(1,tests+1):
	buffer=raw_input()
	buffer=buffer.rsplit()
	n=int(buffer[0])
	m=int(buffer[1])
	filesystem={}

	for i in range(n):
		buffer=raw_input()
		buffer=buffer.rsplit('/')

		tree=filesystem
		for j in buffer:
			if j=='':
				continue
			if(not tree.has_key(j)):
				tree[j]={}
			tree=tree[j]
			
	criei=0
	
	for i in range(m):
		buffer=raw_input()
		buffer=buffer.rsplit('/')

		tree=filesystem
		for j in buffer:
			if j=='':
				continue
			if(not tree.has_key(j)):
				tree[j]={}
				criei+=1
			tree=tree[j]
				
	print "Case #%d: %d"%(t,criei)
	