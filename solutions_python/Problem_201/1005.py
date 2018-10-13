from heapq import heappush, heappop

# a = 10e18
# print(type(a))
num = int(input())
# print(num)
for i in range(num):
	tmp = input()
	tmp = tmp.split()
	# tmp = [float(k) for k in tmp.split()]
	# print(tmp) 
	# ans = np.array([ float(tmp[0]) ])
	heap = []
	heappush(heap, -float(tmp[0]))
	# print(ans)
	for k in range( int(tmp[1]) - 1 ):
		# ans = np.sort(ans, kind = 'heapsort')
		MAX = -heappop(heap)
		if MAX%2 == 0:
			heappush(heap, -MAX/2)
			heappush(heap, -(MAX/2 - 1))
		else:
			heappush(heap, -(MAX-1)/2)
			heappush(heap, -(MAX-1)/2)

	MAX = -heappop(heap)
	print("Case #", i+1, ":", sep = '', end = ' ')
	if MAX == 0:
		print("0 0")
	elif MAX%2 == 0:
		print(int(MAX/2), int(MAX/2-1))
	else:
		print(int((MAX-1)/2), int((MAX-1)/2))


# a = np.array([2,3,7,0])
# print(np.sort(a))
