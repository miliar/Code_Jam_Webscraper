import copy
import unittest
import time
import math

def readInput(filename):
	'''
	Return a list of test cases
	'''
	f = open(filename)
	numTests = int(f.readline())
	tests = [None] * numTests
	for k in range(numTests):
		(A,B) = [int(x) for x in f.readline().split()]
		tests[k] = (A,B)
	return tests

def writeOutput(filename, results):
	g = open(filename, 'w')
	for i in range(len(results)):
		g.write("Case #{}: {}\n".format(i+1, results[i]))
	g.close()

def isPalindrome(x):
	s = str(x)
	n = len(s)
	for i in range(n/2):
		if s[i] != s[n-i-1]:
			return False
	return True

def countFairAndSquare(endpoints):
	(A, B) = endpoints
	start = int(math.ceil(math.sqrt(A)))
	end = int(math.floor(math.sqrt(B)))
	i = start
	count = 0
	while i <= end:
		if isPalindrome(i) and isPalindrome(i*i):
			count += 1
		i += 1
	return count

def solveAll(testId):
	tests = readInput(testId + '.in')
	results = [countFairAndSquare(test) for test in tests]
	writeOutput(testId + '.out', results)

class IsPalindromeTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(True, isPalindrome(1))

	def test2(self):
		self.assertEqual(True, isPalindrome(101))

	def test3(self):
		self.assertEqual(True, isPalindrome(801939108))

	def test4(self):
		self.assertEqual(False, isPalindrome(10))

	def test5(self):
		self.assertEqual(False, isPalindrome(1234564321))

	def test6(self):
		self.assertEqual(False, isPalindrome(12345764321))

def checkPalindromeTime():
	N = 10000000
	t1 = time.time()
	palindromes = set()
	i = 1
	while i <= N:

		if isPalindrome(i):
			palindromes.add(i)
		i += 1
	print(len(palindromes))
	t2 = time.time()
	print(t2-t1)

if __name__ == '__main__':
#	suite = unittest.TestLoader().loadTestsFromTestCase(IsPalindromeTest)
#	unittest.TextTestRunner(verbosity=2).run(suite)

#	checkPalindromeTime()

#	solveAll('sample')
	solveAll('C-small-attempt0')

