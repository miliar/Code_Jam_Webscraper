#!/usr/bin/python
import sys
import re
def main():
	f=open(sys.argv[1])
	n=int(f.readline()[:-1])
	mainstr="welcome to code jam"
	for i in range(0,n):
		#line=removeunwanted(mainstr,f.readline()[:-1])
		#print line
		line=f.readline()[:-1]
		ctr=0
		if re.match(buildpat(mainstr),line):
			ctr=count(mainstr,line)
		sctr=("%04d" % (ctr))[-4:]
		print "Case #%d: %s" % (i+1,sctr)
				
def count(tomatchstr,origstr):
	if(len(tomatchstr) == 0):
		return 1 
	#get first character. find all indexes of it
	if(re.match(buildpat(tomatchstr),origstr)):
		if(len(origstr) <= 1):
			return 1
		c=tomatchstr[0]
		indexes=findallindexes(origstr,c)
		ctr=0
		for index in indexes:
			ctr=ctr+count(tomatchstr[1:],origstr[index+1:])
		return ctr
	else:
		return 0

def findallindexes(tstr,c):
	i=[]
	l=0
	while True:
		if l >= len(tstr):
			break
		if(tstr.find(c,l) == -1):
			break
		else:
			loc=tstr.find(c,l)
			i.append(loc)
			l=loc+1
	return i	


def buildpat(str):
	r=[".*?"]
	for c in str:
		if c == ' ':
			r.append(r"\s.*?")	
		else:
			r.append(c+r".*?")
	return "".join(r)

if __name__ == "__main__":
	main()
