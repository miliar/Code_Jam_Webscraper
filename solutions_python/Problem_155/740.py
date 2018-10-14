#! /usr/bin/python
import sys

def calc(nMax, arrList):
	nReq = 0
	bSum = 0
	#print nMax
	#print arrList
	for i in range(nMax+1):
		if (bSum < i and arrList[i]>0):
			nReq += i-bSum
			bSum = i
		bSum += arrList[i]
		#print i, bSum, nReq
	return nReq

def main(args):
	f = open(args[1], 'r')
	fout = open("ovation.out", 'w')
	nCases = int(f.readline())
	for k in range(nCases):
		line = f.readline()
		nMax = int(line.split(" ")[0])
		arrList = []
		strList = line.split(" ")[1].strip()
		for i in range(nMax+1):
			arrList.append(int(strList[i]))
		nReq = calc(nMax, arrList)
		fout.write("Case #"+str(k+1)+": "+str(nReq)+"\n")

if __name__ == '__main__':
	main(sys.argv)