from heapq import heappush,heappop
def calc(n,k):
	heap = []
	heappush(heap,-1*(n))
	k-=1
	while (k>0):
		k-=1
		large = -1*heappop(heap)
		if large==0 or large==1:
			return "0 0"
		#print large,heap
		if large%2==1:
			heappush(heap,-1*(large/2))
			heappush(heap,-1*(large/2))
		else:
			heappush(heap,-1*(large/2))
			heappush(heap,-1*(large/2-1))
		#print heap
	lg = -1*heappop(heap)
	#print lg
	if lg%2==0:
		ans = (lg/2)-1
		if ans<0:
			ans=0
		ans1 = lg/2
		if ans1<0:
			ans1=0
		return str(ans1)+" "+str(ans)
	else:
		ans1 = lg/2
		if ans1<0:
			ans1=0
		return str(ans1)+" "+str(ans1)


f = open("C-small-2-attempt3.in")
t = int(f.readline())

for i in range(1,t+1):
	x = (f.readline())
	x = x.split()
	#print x
	print("Case #"+str(i)+": "+str(calc(int(x[0]),int(x[1]))))
