import sys

T = int(sys.stdin.readline().strip())

for i in range(1,T+1):
	print 'Case #%d:' %i,
	num = sys.stdin.readline().strip().split()
	A = int(num[0])
	B = int(num[1])
	total = 0
	for j in range(A,B+1):
		count = 0
		reverse = str(j)[::-1]
		if str(j) == reverse:
			count += 1
		square = j**(1.0/2)
		
		if square%1 == 0.0:
			revsquare = str(long(square))[::-1]
			
			if str(long(square)) == revsquare:
				count += 1

		if count == 2:
			total += 1
	print total
