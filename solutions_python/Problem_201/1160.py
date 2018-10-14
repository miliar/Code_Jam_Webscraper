import sys
import heapq
t=input()
for i in range(1,t+1):
	n,k=map(int,raw_input().split())
	print "Case #"+str(i)+":",
	if(n%2==0):
		heap=[-(n/2),-(n-(n/2)-1)]
		if(k==1):
			print (n/2),
			print (n-(n/2)-1)
			continue
	else:
		heap=[-(n/2),-(n/2)]
		if(k==1):
			print (n/2),
			print (n/2)
			continue
	heapq.heapify(heap)
	for j in range(k-2):
		c=-(heapq.heappop(heap))
		if(c%2==0):
			heapq.heappush(heap,-(c-(c/2)-1))
		else:
			heapq.heappush(heap,-(c/2))
		heapq.heappush(heap,-(c/2))
	c=-(heapq.heappop(heap))
	# print c
	if(c%2!=0):
		print c/2,
		print c/2
	else:
		print c/2,
		print c-(c/2)-1
		
		
