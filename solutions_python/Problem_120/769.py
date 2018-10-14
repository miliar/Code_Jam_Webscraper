import os, re, sys, math
import unittest

class Test(unittest.TestCase):
	def test_1(self):
		self.assertEqual(main(1, 9), 1)
	def test_2(self):
		self.assertEqual(main(1, 10), 2)
	def test_3(self):
		self.assertEqual(main(3, 40), 3)
	def test_4(self):
		self.assertEqual(main(1, 1000000000000000000), 707106780)
	def test_5(self):
		self.assertEqual(main(10000000000000000, 1000000000000000000), 49)


#tCase = sys.stdin.readline().split()
tCase = int(sys.stdin.readline())

def main(N, M):
	area_firt = (N + 1) * (N + 1) - (N * N)
	tinta = M - area_firt
	count = 1
	i = 3
	while tinta > 0:
		next = (N + i) * (N + i) - (N + i - 1) * (N + i - 1)
		#print ":::", tinta, next
		if tinta - next >= 0:
			tinta = tinta - next
			count += 1
			
			area_firt = next
			i += 2
		else:
			break
	#print area_firt
	return count
		
 
if __name__ == '__main__':
	#unittest.main()
	for i in xrange(tCase):	
		#frase = [str(x) for x in sys.stdin.readline().split(' ')]	
		#print "Case #%d: %s" % (i + 1, main(frase[0]))
		
		##Numbers
		N,M = [int(x) for x in sys.stdin.readline().split(' ')]	
		print "Case #%d: %d" % (i + 1, main(N,M))