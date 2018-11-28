import numpy as np

def fairSquare(A,B):

	maxB = int(np.sqrt(B))/10
	maxA = int(np.sqrt(A))/10
	count = 0
	if A < 10:
		count = 3
		if A > 4:
			count -= 1
		if A > 1:
			count -= 1
	if B < 9:
		count -= 1
	if B < 4:
		count -= 1

	while maxA <= maxB and maxB > 0:
		x = (maxB + 10*maxB)
		if x*x <= B and x*x >= A:
			count += 1
		maxB -= 1

	return count

def readInput(filename, outname):
	file = open(filename,'r')
	n = int(file.readline())
	out = open(outname,'w')
	for i in xrange(n):
		A, B = file.readline().split('\n')[0].split(' ')
		outstr = "Case #%i: %i" %(i+1,fairSquare(int(A),int(B)))
		out.write(outstr+'\n')
		print outstr
	file.close()
	out.close()

def main():
	readInput('C-small-attempt3.in','C-small-attempt3.out')

if __name__ == "__main__":
	main()