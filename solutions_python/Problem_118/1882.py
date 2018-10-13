#!/urs/bin/env python3
from math import sqrt
def test(x):
	digits = []
	while(x>0):
		digits.append(x%10)
		x //= 10
	for i in range(len(digits)//2+1):
		if digits[i] != digits[-(i+1)]:
			return 0
	return 1

with open ('input.txt') as input:
	input.readline()
	k = 1
	for line in input:
		count = 0
		a, b = map(int, line.split(' '))
		while(a<=b):
			x = sqrt(a)
			if (int(x)==x):
				count += (test(int(x)) & test(a))
			a+=1
		print('Case #{}: {}'.format(k,count))
		k+=1