import math
import sys
from decimal import *

def isTidy(n):
	for i in range(len(n)-1):
		if not n[i] <= n[i+1]:
			return False
	return True

def getTidy(n):
	mul = 10
	while not isTidy(str(n)):
		div = Decimal(n)// Decimal(mul)
		mul_r = div*Decimal(mul)
		sub = mul_r-1
		n = sub

		mul *= 10 

	return n

def main():
	file_in = open(sys.argv[1], "r")
	file_out = open("out", "w")

	T = int(file_in.readline())
	for i in range(1, T+1):
		n = int(file_in.readline())
		tidy_number = getTidy(n)

		out_string = "Case #%d: %d\n" % (i, tidy_number)
		print out_string, 
		file_out.write(out_string)

	file_in.close()
	file_out.close()

if __name__ == '__main__':
	main()