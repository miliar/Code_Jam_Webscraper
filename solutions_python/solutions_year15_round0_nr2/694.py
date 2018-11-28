from collections import deque

class node:
	def __init__(self, n, arr):
		self.n = n
		self.arr = arr
	def allEmpty(self):
		for i in self.arr:
			if i > 0:
				return False
		return True
	def __str__(self):
		return str(self.n) + str(self.arr)



T = int(raw_input())

for case in xrange(1, T + 1):

	N = int(raw_input())
	arr = map(int, raw_input().split())
	q = deque()
	q.append(node(0, arr))

	ans = 0
	while len(q) != 0:

		top = q.popleft()

		# op1
		arr = top.arr[:]
		for i in xrange(len(arr)):
			if arr[i] > 0:
				arr[i] -= 1
		newNode = node(top.n + 1, arr) 

		if newNode.allEmpty():
			ans = newNode.n
			break

		q.append(newNode)

		# op2
		first = max(top.arr)

		for i in xrange(1, 1 + first / 2):
			arr = top.arr[:]
			arr.remove(first)
			arr.append(i)
			arr.append(first - i)

			q.append(node(top.n + 1, arr))


	print 'Case #%d: %d' % (case, ans)