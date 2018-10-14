#!/usr/bin/python
import sys
import re
def testtraverse(gr,tokens):
	nodes=gr
	for i in range(0,len(tokens)):
		cnt=False
		for c in tokens[i]:
			if c == nodes[i]:
				cnt=True
				break
		if cnt:
			continue
		else:
			return False
	return True

lenargs=2		
if len(sys.argv) < lenargs:
	print "Usage: %s <file>" % (sys.argv[0])
	exit(128)
f=open(sys.argv[1])
s = f.readline().split(" ")
l = int(s[0])
d=int(s[1])
n=int(s[2])
graphs=[]
for i in range(0,d):
	s=f.readline()[:-1]
	gr=[]
	graphs.append(gr)
	parent=s[0]
	gr.append(parent)
	for j in range(1,l):
		node=s[j]
		gr.append(node)
pat=re.compile(r"\(([a-z]+?)\)|([a-z])")

for i in range(0,n):
	s=f.readline()[:-1]
	tokens=[t[0] if t[0] else t[1] for t in pat.findall(s)]		
	ctr=0
	for gr in graphs:
		if testtraverse(gr,tokens):
			ctr=ctr+1
	print "Case #%d: %d" % (i+1,ctr)
	
f.close()
