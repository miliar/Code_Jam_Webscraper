import sys
from collections import namedtuple
import heapq

class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val


def solve(n, k):
	h = MaxHeap()

	h.heappush(n)

	mn, mx = 0, 0
	for i in xrange(k):
		r = h.heappop()

		r1 = r / 2

		if r % 2 != 0:
			r1 = r / 2
			r2 = r / 2
		else:
			r1 = r / 2
			r2 = r1-1


		h.heappush(r1)
		h.heappush(r2)

		mx, mn = max(r1, r2), min(r1, r2)

		# print 'r1 = {}, r2 = {}'.format(r1, r2)
	# print h.heappop()

	return '{} {}'.format(mx, mn)

def main():
	f = open(sys.argv[1], 'rb')

	tests = int(f.readline().strip())

	ret = []
	for test in xrange(tests):
		print "test = {}".format(test)
		n, k = f.readline().strip().split()
		n, k = int(n), int(k)
		ret.append(solve(n, k))
		# break

	for i, nums in enumerate(ret):
		print "Case #{}: {}".format(i+1, nums)


if __name__ == '__main__':
	main()