'''
Created on May 8, 2010

@author: indra
'''
import sys, os

filename = "A-large"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")

ar = [-1,1]
for n in xrange(2,33):
	ar.append(2*ar[n-1]+1)
	
#print ar

cases = int(reader.readline().rstrip())

#print cases

caseno = 1
while caseno<=cases:
	case = reader.readline().rstrip()
	#print case
	N,K = [int(x) for x in case.split(' ')]
	#print (N,K)
	bal = K%(ar[N]+1)
	#print bal

	if bal==ar[N]:
		writer.write("Case #"+str(caseno)+": ON\n")
	else:
		writer.write("Case #"+str(caseno)+": OFF\n")
	caseno+=1


writer.close()