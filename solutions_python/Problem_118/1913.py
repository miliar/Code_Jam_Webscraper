#! /usr/bin/python
import sys
import math
def checkStatus(example,startNum,endNum,output):
	count = 0
	a = int(math.ceil(math.sqrt(startNum)))
	b = int(math.floor(math.sqrt(endNum)))
	#print 'a is '+str(a)+' b is '+str(b)
	for i in range(a,b+1):
		if(checkPa(i) and checkPa(i**2)):
			count = count +1 
			#print(i)
			#print(i**2)
	#print 'count is'+str(count)
	output.write('Case #%d: %d\n'% (example+1,count))
	return
def checkPa(num):
	strnum = str(num)
	L = len(strnum)
	for i in range(0,L):
		if(strnum[i]!=strnum[L-1-i]):
			return 0
	return 1
				
def myprint(list1):
	for item in list1:
		print item
		print('\n')					
def fair(filename):
	f = open(filename)
	line = f.readline()
	numOfSamples = int(float(line.strip()))
	#print(numOfSamples)
	for example in range(0,numOfSamples):
		list_outer = []
		line = f.readline()
		line = line.strip()
		L = line.split(' ')
		startNum = int(L[0])
		endNum = int(L[1])
		#print startNum
		#print endNum
		checkStatus(example,startNum,endNum,sys.stdout)
		
		
def main():
	fair('C-small-attempt0.in')
	#fair('testcase1.txt')
	#print(checkPa(11))
	#print(checkPa(121))

if __name__ == '__main__':
	main()
