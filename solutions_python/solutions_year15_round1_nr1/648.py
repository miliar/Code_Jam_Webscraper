import numpy as np
f = open('input.txt', 'r')

def function(shrooms):
	x = 0
	y = 0
	maximum = max(0, shrooms[0] - shrooms[1])

	for i in xrange(len(shrooms) - 1):
		rate = shrooms[i] - shrooms[i+1]
		if rate > maximum:
			maximum = rate

	for i in xrange(len(shrooms) - 1):
		if shrooms[i + 1] < shrooms[i]:
			x += shrooms[i] - shrooms[i + 1]

	for i in xrange(len(shrooms) - 1):
		# print(y, shrooms[i])
		if shrooms[i] > maximum:
			y += maximum
		else:
			y += shrooms[i]
	return str(x) + " " + str(y)


T = int(f.readline())
for i in xrange(T):
	temp = f.readline()
	shrooms = map(int, f.readline().split(' '))
	
	print("Case #" + str(i+1) + ": " + function(shrooms))

