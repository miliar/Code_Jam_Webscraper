from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)

fp = open(os.path.join(directory, files[0]), 'rb')
fp2 = open(os.path.join(directory, '..', 'out2.txt'), 'wb')

lines = iter(map(lambda x: x.strip(), fp.readlines()))

# functions go here
def gcd(a, b):
    if a == 0:
       return b
    while b != 0:
        if a > b:
           a = a - b
        else:
           b = b - a
    return a

tests = int(next(lines))
for i in range(tests):
	n, l, h = map(int, next(lines).split())
	d = map(int, next(lines).split())
	
	b = False
	for x in range(l, h+1):
		b = len(filter(lambda y: x % y == 0 or y % x == 0, d)) == len(d)
		if b:
			break

	print('Case #%d: %s' % (i+1, (str(x) if b else 'NO')), file=fp2)

fp.close()
fp2.close()
