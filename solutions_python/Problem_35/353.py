#!/usr/bin/python
import sys
def main():
	lenargs=2
	if len(sys.argv) < lenargs:
		print "Usage: %si ipfile" % (sys.argv[0])
		exit(128)
	f=open(sys.argv[1])
	t=int(f.readline())
	
	for testcase in range(0,t):
		print "Case #%d:" % (testcase+1)
		s=f.readline()[:-1].split(" ")
		l=int(s[0])
		w=int(s[1])
		#print "%d %d" % (l,w)
		altmap=[[int(x) for x in f.readline()[:-1].split(" ")] for i in range(0,l)]
		
		#print altmap
		assigned=set([])
		printmap=[["x" for x in row] for row in altmap]
		sinks=[]
		for i in range(0,l):
		    for j in range(0,w):
		        if (i,j) not in assigned:
		            assignsink(altmap,i,j,l,w,assigned,sinks,printmap)
		labels={}
		last=""
		for i in range(0,l):
			toprint=""
			for j in range(0,w):
			    if printmap[i][j] in labels.keys():
			    	toprint=toprint+labels[printmap[i][j]]+" "
			    else:
			    	if not last:
			    		last="a"
			    	else:
				    	last=chr(ord(last)+1)
			    	labels[printmap[i][j]] = last
			    	toprint=toprint+last+" "
			toprint=toprint[:-1]
			print toprint
def assignsink(altmap,i,j,l,w,assigned,sinks,printmap):
	if i < 0 or i >= l:
		return
	if j < 0 or j>= w:
		return
	myalt=altmap[i][j]
	min=myalt
	if not issink(altmap,i,j,l,w):
		mindir=None
		if getalt(altmap,i-1,j,l,w) < min:
			min=getalt(altmap,i-1,j,l,w)
			mindir=(i-1,j)
		if getalt(altmap,i,j-1,l,w) < min:
			min=getalt(altmap,i,j-1,l,w)
			mindir=(i,j-1)
		if getalt(altmap,i,j+1,l,w) < min:
			min=getalt(altmap,i,j+1,l,w)
			mindir=(i,j+1)            
		if getalt(altmap,i+1,j,l,w)  < min:
			mindir=(i+1,j)
		printmap[i][j]=assignsink(altmap,mindir[0],mindir[1],l,w,assigned,sinks,printmap)
		assigned.add((i,j))
		return printmap[i][j]
	else:
		if (i,j) not in sinks:
			sinks.append((i,j))
		printmap[i][j]=(i,j)
		return (i,j)
		
def issink(altmap,i,j,l,w):
    myalt=altmap[i][j]
    return getalt(altmap,i-1,j,l,w) >= myalt and getalt(altmap,i+1,j,l,w) >= myalt and getalt(altmap,i,j-1,l,w) >= myalt and getalt(altmap,i,j+1,l,w) >= myalt
    
def getalt(altmap,i,j,l,w):
	if i < 0:
		return sys.maxint
	if j < 0:
		return sys.maxint
	if i >= l:
		return sys.maxint
	if j >= w:
		return sys.maxint
	return altmap[i][j]
	
if "__main__" == __name__:
	main()
