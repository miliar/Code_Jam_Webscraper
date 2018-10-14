from math import *
from decimal import *
from decimal import Decimal as D

def case(n):
	r, t = map(int, input().split(' '))
	
	r = Decimal(r)
	t = Decimal(t)
	
	getcontext().prec = 30
	
	print ('Case #%d: %s' % (n, int((D(1)-D(2)*r+(D(1)-D(4)*r+D(4)*r*r+D(8)*t).sqrt())/D(4))))

if __name__ == '__main__':
	for i in range(int(input())):
		case(i + 1)