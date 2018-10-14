#encoding: utf-8
import sys
def main():
	inputFile = open(sys.argv[1],'r')
	nTest = int(inputFile.readline())
	for i in range(1,nTest+1):
		line1 = inputFile.readline()
		a = line1.strip().split()
		maxShy = int(a[0])
		#print maxShy, a[1], a[1][maxShy]
		valSum = 0
		prevSum = 0 
		result = 0
		for k in range(len(a[1])):
			currVal = int(a[1][k])
			currPos = k 
			#print currPos
			if currVal != 0:
				if currPos != prevSum and currPos > prevSum:
					result = result + (currPos-prevSum)
					prevSum = prevSum + result  
			prevSum = prevSum + currVal
		print "Case #" + str(i) +": " + str(result)	




if __name__ == '__main__':
	main()