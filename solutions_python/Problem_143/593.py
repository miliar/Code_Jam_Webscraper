from collections import *

inFile = open("input.txt", "r")

outFile = open("out.txt", "w")

T = int(inFile.readline())

for t in xrange(T):
	outFile.write("Case #" + str(t+1) + ": ")
	kk = inFile.readline()
	a,b,k = [ int(i) for i in kk.rstrip().split(" ")]
	cnt = 0
	for i in xrange(a):
		for j in xrange(b):
			if i & j < k:
				cnt+=1
	outFile.write(str(cnt))


	outFile.write("\n")

