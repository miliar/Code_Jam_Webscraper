from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)

fp = open(os.path.join(directory, files[0]), 'rb')
fp2 = open(os.path.join(directory, '..', 'out1.txt'), 'wb')

lines = iter(map(lambda x: x.strip(), fp.readlines()))

# functions go here

tests = int(next(lines))
for i in range(tests):
	total = 0
	x,s,r,t,n = map(int, next(lines).split())
	w = []
	nw = x
	for j in range(n):
		a,b,ws = map(int, next(lines).split())
		nw -= b-a
		w.append([b-a, ws])
		#read data and execute
		#pass

	w.append([nw, 0])
	
	w.sort(key=lambda x: x[1])
	
	for k in w:
		if t > 0:
			time = float(k[0]) / (k[1] + r)
			if time <= t:
				total += time
				t -= time
			else:
				total += t
				total += float(k[0] - t*(k[1] + r)) / (k[1] + s)
				t = 0
		else:
			total += float(k[0]) / (k[1] + s)
	
	print('Case #%d: %f' % (i+1, total), file=fp2)

fp.close()
fp2.close()
