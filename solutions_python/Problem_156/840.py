import sys
import math

restaurant_queue = []

sys.setrecursionlimit(10000)

primes = [2,3,5,7,11,13,17,19,23,29,31]

class Restaurant:
	def __init__(self, diners, level):
		self.diners = diners
		self.level = level
		self.tree = None

	def __repr__(self):
		return 'level: ' + str(self.level) + ' diners: ' + str(self.diners)

	def is_finished(self):
		return sum(self.diners) == 0

def wait(restaurant):
	temp = list(restaurant.diners)
	for i in xrange(len(temp)): #wait
		if temp[i] > 0:
			temp[i] -= 1
	return Restaurant(temp, restaurant.level+1)

def special(restaurant, n):
	temp = sorted(restaurant.diners, key=int, reverse=True)
	t = temp[0]
	temp[0] /= n
	temp.append(t - temp[0])
	return Restaurant(temp, restaurant.level+1)

def create_tree(restaurant):
	restaurant_queue.append(wait(restaurant))
	for n in [k for k in primes if k <= math.sqrt(max(restaurant.diners))]:
		restaurant_queue.append(special(restaurant,n))
	temp = restaurant_queue.pop(0)
	if temp.is_finished():
		return temp.level
	else:
		return create_tree(temp)

if __name__ == '__main__':
	f = open(sys.argv[1])

	T = int(f.readline())

	for case in xrange(1,T+1):
		restaurant_queue = []
		D = int(f.readline())
		diners = [int(d) for d in f.readline().split(' ')] + [0]
		r = Restaurant(diners, 0)		
		minutes = create_tree(r)
		print 'Case #%d: %d' % (case, minutes)