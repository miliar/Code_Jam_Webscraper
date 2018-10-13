'''
Created on April 14, 2012

@author: indra
'''
import sys, os

filename = "C-small-attempt2"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

cases = int(reader.readline().rstrip())

def isRecycled(n,m):
	if(n>=m):
		return False
	if len(str(n))!=len(str(m)):
		return False
	else:
		strn = str(n)
		#print "-----",n,"  ",m
		for i in range(len(strn)):
			recn = strn[i:len(strn)]+strn[:i]
			if int(recn)==m:
				#print recn
				return True
	return False
#print cases
map=[[] for i in range(1000)]
for i in range(1000):
	map[i] = [isRecycled(i,j) for j in range(1001) ]
caseno = 1
while caseno<=cases:
	case = reader.readline().rstrip()
	A,B = [int(x) for x in case.split(' ')]
	count = 0
	for n in range(A,B):
		for m in range(n+1,B+1):
			if map[n][m]:
				#print m,"---",n
				count+=1

	writer.write("Case #"+str(caseno)+": "+str(count)+"\n")
	caseno+=1


writer.close()