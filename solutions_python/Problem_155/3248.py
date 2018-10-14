#!/usr/bin/env python

def probA(maxshy,shy):
	if shy.find("0")==-1:
		return 0
	s=0
	friends=0
	for i in xrange(len(shy)):
		if s<i:
			friends+=1
			s+=1
		s+=int(shy[i])
	return friends

def main():
	fin=open("A-large.in","r")
	fout=open("testAResL.txt","w")
	numTests=int(fin.readline())
	print "numTests",numTests
	for i in xrange(numTests):
		l=fin.readline().split()
		res=probA(int(l[0]),l[1])
		print l,res
		fout.write("Case #%d: %d\n" % (i+1,res))
	fin.close()
	fout.close()





















main()
