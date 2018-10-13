import os, re, sys
import math
import unittest

class Test(unittest.TestCase):
	def test_1(self):
		self.assertEqual(main([2,2,2]), "GABRIEL")
	def test_2(self):
		self.assertEqual(main([2,1,3]), "RICHARD")
	def test_3(self):
		self.assertEqual(main([4,4,1]), "RICHARD")
	def test_4(self):
		self.assertEqual(main([3,2,3]), "GABRIEL")
	def test_5(self):
		self.assertEqual(main([4,4,3]), "GABRIEL")
#tCase = sys.stdin.readline().split()
tCase = int(sys.stdin.readline())

def main(M):
	if M[0] == 1:
		return "GABRIEL"
	elif M[0] == 2:
		if (M[1] % 2 == 0 and M[2] >= 1) or (M[2] % 2 == 0 and M[1] >= 1):
			return "GABRIEL"
	elif M[0] == 3:
		if (M[1] % 3 == 0 and M[2] >= 2) or (M[2] % 3 == 0 and M[1] >= 2):
			return "GABRIEL"
	elif M[0] == 4:
		if (M[1] % 4 == 0 and M[2] >= 3) or (M[2] % 4 == 0 and M[1] >= 3):
			return "GABRIEL"
	return "RICHARD"
		
if __name__ == '__main__':
	#unittest.main()
	for i in xrange(tCase):	
		#frase = [str(x) for x in sys.stdin.readline().split(' ')]	
		#print "Case #%d: %s" % (i + 1, main(frase[0]))
		
		##Numbers
		M = [int(x) for x in sys.stdin.readline().split(' ')]
		print "Case #%d: %s" % (i + 1, main(M))