#! /usr/bin/python
import sys

def checkStatus(example,rows,N,M,output):
	# N is number of rows
	# M is number of cols 
	cols = zip(*rows)
	for i in range(0,N):
		for j in range(0,M):
			if((rows[i][j]!=max(rows[i])) and (cols[j][i]!=max(cols[j]))):
				output.write ( 'Case #%d: NO\n'% (example+1))
				return
	output.write('Case #%d: YES\n'% (example+1))
	return
		
def myprint(list1):
	for item in list1:
		print item
		print('\n')					
def lawns(filename):
	f = open(filename)
	line = f.readline()
	numOfSamples = int(float(line.strip()))
	#print(numOfSamples)
	for example in range(0,numOfSamples):
		list_outer = []
		line = f.readline()
		line = line.strip()
		L = line.split(' ')
		N = int(L[0])
		M = int(L[1])
		for row in range(0,N):
			line = f.readline()
			line = line.strip()
			l = line.split(' ')
			l = [int(element) for element in l]
			list_outer.append(l)
		checkStatus(example,list_outer,N,M,sys.stdout)
		
def main():
	lawns('B-small-attempt3.in')
	#lawns('testcase1.txt')

if __name__ == '__main__':
	main()
