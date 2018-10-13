import sys
import time
import math
from decimal import Decimal
from itertools import product
from time import clock

#reverse the string
# def my_str_rev(str):
# 	return str[::-1]

def fetch(a, b):
	while a <= b:
		yield a
		a += 1


def main(argv):
	''' The main function '''
	#open the file
	with open(argv[1]) as f:
		#number of testcases
		T = int(f.readline().rstrip())
		lines = iter(f.readlines())

		my_list = []
		for num in fetch(1, long(10**7)):
			# print "Entered"
			temp = str(num)
			# print temp
			if temp == temp[::-1]:
				sq = str(num*num)
				if sq == sq[::-1]:
					my_list.append(long(sq))

		for i in xrange(1, T + 1):	
			AB = lines.next().rstrip().split(" ")

			a = AB[0]
			b = AB[1]

			count = 0
	
			a = long(a)
			b = long(b)

			new_list = [e for e in my_list if e >= a and e <= b]
			
				# print count, a
			
			print "Case #%d: %d" % (i, len(new_list))
			

if __name__ == "__main__":
	main(sys.argv)