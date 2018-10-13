import math
from decimal import *
def main():
	# r, t = ( Decimal(i) for i in input().split())
	# x = Decimal(1)+(Decimal(9)+Decimal(4)*(r*r-r+Decimal(2)*t-Decimal(2))).sqrt()
	# print(((x / Decimal(2) - r) / Decimal(2)))
	#r, t = ( int(i) for i in input().split())
	#x = -2*r+1+math.sqrt(1+4*(r*r-r+2*t))
	#print(x / 4)
	getcontext().prec = 50
	r, t = ( Decimal(i) for i in input().split())
	x = Decimal('-2')*r+Decimal('1')+(Decimal('1')+Decimal('4')*(r*r-r+Decimal('2')*t)).sqrt()
	print(math.floor(x / Decimal(4)))


T = int(input())
for i in range(T):
	print("Case #{:d}: ".format(i+1),end='')
	main()