#!/usr/bin/python
import sys
import math
import time

def is_fair(a):
	t = a
	b = 0
	if a % 10 == 0:
		return False
	while t > 9:
		b = b*10 + t%10
		t /= 10
	b = b*10 + t
	return a == b

def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)>>1
        if y >= x:
            return x
        x = y

f = open(sys.argv[1]);
T = int(f.readline())
i = 0

for line in f.readlines():
	i += 1
	A, B = line.split()
	A, B = int(A), int(B)

	a = isqrt(A)
	b = isqrt(B)
	t = a + 1
	if a**2 == A:
		t = a
	found = 0
	while t <= b:
		if is_fair(t):
			if is_fair(t**2):
				found += 1
		t += 1
	print "Case #{}: {}".format(i, found)

f.close()