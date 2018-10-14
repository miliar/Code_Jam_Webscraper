import heapq
import math

class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

def splitNode(number):
	if number == 1:
		return 0, 0
	if number == 0:
		return 0, 0
	if number % 2 == 0:
		return number / 2, (number / 2) - 1
	else:
		return (number - 1) / 2, (number - 1) / 2

def doWork(bathroomStalls, people):
	if bathroomStalls * 0.9 < people:
		return (0, 0)

	maxh = []
	heapq.heappush(maxh,MaxHeapObj(bathroomStalls))

	for person in range(people):
		todo = heapq.heappop(maxh).val 
		if todo == 1:
			return (0, 0)
		maxim, minim = splitNode(todo)
		heapq.heappush(maxh,MaxHeapObj(maxim))
		heapq.heappush(maxh,MaxHeapObj(minim))
	return (maxim, minim)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	inputArray = [int(s) for s in raw_input().split(" ")]
	bathroomStalls = inputArray[0]
	people = inputArray[1]
	out = doWork(bathroomStalls, people)
	print "Case #{}: {} {}".format(i, out[0], out[1])
