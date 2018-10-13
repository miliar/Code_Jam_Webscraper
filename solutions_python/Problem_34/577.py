import psyco
psyco.full()

import re

def main():
	l,d,n=map(lambda x:int(x),raw_input().split())
	linput=[]
	tclist=[]

	for i in xrange(d):
		words=raw_input()
		linput.append(words)

	for i in xrange(n):
		words=raw_input()
		words=words.replace("(","[")
		words=words.replace(")","]")
		tclist.append(words)
	
	loutput=[0]*len(tclist)
	
	for k,i in enumerate(tclist):
		for j in linput:
			a=re.findall(i,j)
			if a==[]:
				continue
				
			elif a[0]==j:
				loutput[k]+=1
			
	for i,j in enumerate(loutput):
		print "Case #%d: %d"%(i+1,j)
	
main()	
