#!/usr/bin/python
import sys
debug=False
def debugop(s):
	global debug
	if debug:
		print s
f=open(sys.argv[1])
if len(sys.argv) > 2:
	if(sys.argv[2] == "y"):
		debug=True
tc=int(f.readline().strip())
for i in range(0,tc):
	l=f.readline().strip()
	if not l:
		continue
	vals = l.split()
	debugop(vals)
	vi=0
	c=int(vals[vi])
	vi=vi+1
	combines={}
	for j in range(0,c):
		e1=vals[vi][0]
		e2=vals[vi][1]
		re=vals[vi][2]
		combines[e1+e2]=re
		combines[e2+e1]=re
		vi=vi+1
	d=int(vals[vi])
	vi=vi+1
	opposes=set()
	for j in range(0,d):
		e1=vals[vi][0]
		e2=vals[vi][1]
		opposes.add(e1+e2)
		opposes.add(e2+e1)
		vi=vi+1
	n=int(vals[vi])
	netellist=[]
	els=vals[vi+1]
	debugop("combines=%s , opposes = %s , els = %s" % (str(combines),str(opposes),str(els)))
	for j in range(0,n):
		debugop(els[j])
		netellist.append(els[j])
		combined = False
		if len(netellist) >= 2 and combines.has_key(netellist[len(netellist)-1]+netellist[len(netellist)-2]):
			debugop("Combining")
			nbe=combines[netellist[len(netellist)-1]+netellist[len(netellist)-2]]
			netellist = netellist[:-2]
			netellist.append(nbe)
			combined=True
		if not combined and len(netellist) >= 2:
			for el2 in netellist[:-1]:
				if els[j]+el2 in opposes:
					debugop("Reducing")
					netellist=[]
					break
		debugop("netellist=%s" % ("["+", ".join(netellist)+"]"))
	print "Case #%d: %s" % (i+1,"["+", ".join(netellist)+"]")