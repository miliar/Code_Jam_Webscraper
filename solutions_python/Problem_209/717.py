#encoding=utf8
import math

class Pancake:
	def __init__(self, rr, hh, ii):
		self.index = ii
		self.r = rr
		self.h = hh
		self.hsize = 2*math.pi*rr*hh


filename = "A-large.in"
raw_data = ''
with open(filename, 'r') as f:
	raw_data = f.read().split('\n')

test_count = int(raw_data.pop(0))
for test in range(test_count):
	data = raw_data.pop(0).split(' ')
	numbers = int(data.pop(0))
	dishes = int(data.pop(0))

	lists = []
	for count in range(numbers):
		data2 = raw_data.pop(0).split(' ')
		pp = Pancake(int(data2.pop(0)), int(data2.pop(0)), count)
		lists.append(pp)

	lists.sort(key=lambda pancake: pancake.hsize)

	result = 0 
	maxSurface = 0
	for count in xrange(dishes-1):
		pp = lists.pop()
		result += pp.hsize
		if pp.r*pp.r*math.pi > maxSurface:
			maxSurface = pp.r*pp.r*math.pi
			maxpp = pp

	tempmax = result
	for count in xrange(len(lists)):
		pp = lists[count]
		v1 = pp.r*pp.r*math.pi+pp.hsize

		curmax = v1 + result if v1 + result > (pp.hsize + maxSurface + result) else (pp.hsize + maxSurface + result)
		tempmax = curmax if curmax > tempmax else tempmax 

	print 'Case #%d: %.9f'%(test+1, tempmax)