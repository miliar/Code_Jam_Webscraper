from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)

fp = open(os.path.join(directory, files[0]), 'rb')
fp2 = open(os.path.join(directory, '..', 'out3.txt'), 'wb')

lines = iter(map(lambda x: x.strip(), fp.readlines()))

# functions go here

tests = int(next(lines))

for i in range(tests):
	a = map(int, next(lines).split())
	L, t, N, C = a[:4]
	a = a[4:]
	d = a * (N+1)
	d = map(lambda x: x*2, d[:N])
	
	s=0
	rd = []
	for j, x in enumerate(d):
		s = s + x
		if s - t >= 0:
			rd = d[j:]
			if s - t > 0:
				rd[0] = (s - t)
			break
	
	rd.sort(reverse=True)
	off = sum(rd[:L]) / 2
	
	time = sum(d) - off
	
	print('Case #%d: %d' % (i+1, time), file=fp2)

fp.close()
fp2.close()
