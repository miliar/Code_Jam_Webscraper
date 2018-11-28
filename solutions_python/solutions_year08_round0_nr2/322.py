from heapq import heappush, heappop, heapify

def transform(x):
	return int(x[:2])*60+int(x[3:])

def process():
	
	T = int(raw_input()) # Turnaround time

	NA, NB = [int(x) for x in raw_input().split()]
	
	queue = [] # Heap of tuples (time, action : 0 -> A+, 1 -> A-, 2 -> B+, 3 -> B-)

	RETa = 0
	RETb = 0

	A = 0
	B = 0

	for i in range(0, NA):
		dep, arr = raw_input().split()
		queue.append((transform(dep), 1))
		queue.append((transform(arr) + T, 2))

	for i in range(0, NB):
		dep, arr = raw_input().split()
		queue.append((transform(dep), 3))
		queue.append((transform(arr) + T, 0))

	heapify(queue) # Doing so instead heappushing everything due to O(n) vs O(n log n)

	while queue:
		time, action = heappop(queue)

		if action == 0:
			A += 1
		elif action == 2:
			B += 1
		elif action == 1:
			if A:
				A -= 1
			else:
				RETa += 1
		elif action == 3:
			if B:
				B -= 1
			else:
				RETb += 1
		

	return '%i %i' % (RETa, RETb)

N = int(raw_input())

for i in range(1,N+1):
	print 'Case #%i:'%i, process()
