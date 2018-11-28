import heapq
import collections


def calc2(n, k):
	left = right = None
	heap = []
	heapq.heappush(heap, (-n, 0))
	while heap and k > 0:
		n, i = heapq.heappop(heap)
		n = -n
		left = n / 2 - (1 if n % 2 == 0 else 0)
		right = left + (1 if n % 2 == 0 else 0)
		pos = i + left
		if left != 0:
			heapq.heappush(heap, (-left, i))
		if right != 0:
			heapq.heappush(heap, (-right, pos+1))
		if left == right == 0:
			break
		k -= 1

	if left != None and right != None:
		return "%d %d" % (max(left, right), min(left, right))


def calc(n, k):
	mp = collections.defaultdict(int)
	heap = []
	heapq.heappush(heap, -n)
	mp[n] = 1
	tempSet = set(heap)
	while k > 0:
		i = -heapq.heappop(heap)
		tempSet.remove(-i)
		x = mp[i]
		k -= x
		
		i -= 1
		l = i / 2
		r = l + (i % 2 == 1)
		if k <= 0:
			return "%d %d" % (max(l, r), min(l, r))

		if -l not in tempSet:
			tempSet.add(-l)
			heapq.heappush(heap, -l)
		if -r not in tempSet:
			tempSet.add(-r)
			heapq.heappush(heap, -r)
		
		mp[l] += x
		mp[r] += x

	return None




def test():
	for t in xrange(input()):
		n, k = map(int, raw_input().split())
		print "Case #%d:" % (t + 1), calc(n, k)
		#print calc(n, k)

def test2():
	n = 1000
	for k in xrange(1, n + 1):
	#print "Case #%d:" % (t + 1), calc(n, k)
		x, y = calc2(n, k), calc(n, k)
		if x != y:
			print calc2(n, k), calc(n, k), "(%d, %d)" % (n,k)


test()