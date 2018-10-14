'''
Created on 2013-04-13

@author: ashwin
'''

import math

def isPalindrome(n):
	n = str(n)
	return n == n[::-1]

def numFAS(lowerBound, upperBound):
	answer = 0
	for num in xrange(int(math.ceil(math.sqrt(lowerBound))), int(math.floor(math.sqrt(upperBound)))+1):
		answer += isPalindrome(num) and isPalindrome(num**2)
	return answer

def run(infilepath, outfilepath):
	with open(infilepath) as infile, open(outfilepath, 'w') as outfile:
		T = int(infile.readline().strip())
		for case in xrange(1, T+1):
			lowerBound, upperBound = map(int, infile.readline().split())
			outfile.write("Case #%d: %d\n" %(case, numFAS(lowerBound, upperBound)))

if __name__ == "__main__":
	print 'starting'
	run('/Users/ashwin/Desktop/C-small-attempt0.in', '/Users/ashwin/Desktop/testout.txt')
	print 'done'