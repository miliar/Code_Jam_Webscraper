class maxHeap(object):

	def __init__(self):
		self.mH = [(0,0)]

	def diff(self,x):
		return x[1] - x[0]

	def insert(self,x):
		self.mH.append(x)
		self.bubbleUp()
		if self.mH[-1] == (0,0):
			self.mH.pop()

	def bubbleUp(self):
		pos = len(self.mH)-1
		while pos > 0 and self.diff(self.mH[pos//2]) < self.diff(self.mH[pos]):
			self.mH[pos], self.mH[pos//2] = self.mH[pos//2], self.mH[pos]
			pos //= 2

	def extractMax(self):
		ret = self.mH[0]
		self.mH[0] = self.mH[-1]
		self.mH.pop()
		self.sinkDown(0)
		return ret

	def sinkDown(self, k):
		smallest = k
		l = len(self.mH)

		if smallest == 0:
			if 1 < l and self.diff(self.mH[smallest]) < self.diff(self.mH[1]):
				smallest = 1

			if 2 < l and self.diff(self.mH[smallest]) < self.diff(self.mH[2]):
				smallest = 2

			if smallest != k:
				self.mH[smallest], self.mH[k] = self.mH[k], self.mH[smallest]
				self.sinkDown(smallest)
		else:
			if 2*k < l and self.diff(self.mH[smallest]) < self.diff(self.mH[2*k]):
				smallest = 2*k

			if 2*k+1 < l and self.diff(self.mH[smallest]) < self.diff(self.mH[2*k+1]):
				smallest = 2*k+1

			if smallest != k:
				self.mH[smallest], self.mH[k] = self.mH[k], self.mH[smallest]
				self.sinkDown(smallest)
				
	def display(self):
		for i in range(len(self.mH)):
			print (self.mH[i],)
		print ()

	def display_max(self):
		print (self.mH[0])


t = int(input().strip())
for i in range(1,t+1):
	n,k = map(int,input().strip().split())
	if n == k:
		print ("Case #{}: {} {}".format(i,0,0))
		continue
	h = maxHeap()
	h.insert((0,n+1))
	for j in range(k):
		x,y = h.extractMax()
		m = (x+y)//2
		if j+1 < k:
			if x+1 < m: h.insert((x,m))
			if m+1 < y: h.insert((m,y))
		else:
			a = m-x-1
			b = y-m-1
			print ("Case #{}: {} {}".format(i,max(a,b),min(a,b)))
