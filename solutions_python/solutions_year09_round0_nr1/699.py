import sys
import re

count = 0

def main():
	L = []
	C = []
        f = open('sampleA.in','r')
        line1=f.readline()
       	lengthL,linesD,casesN = line1[:-1].split(' ')
        #print lengthL,linesD,casesN
	Nlinesd = int(linesD)
	Ncasesn = int(casesN)
	for i in range(Nlinesd):
		linese=f.readline()
		realline = linese[:-1]
		L.append(realline)
	#print L	
	for j in range(Ncasesn):
		casesn=f.readline()
		realcase = casesn[:-1]
		C.append(realcase)
	#print C
	for j in range(Ncasesn):
		count = 0
		for i in range(Nlinesd):
			result = re.search(C[j],L[i])
			if result != None:
				count += 1	
		print "Case #%s: %s" % (j+1,count) 
if __name__ == '__main__': main()
