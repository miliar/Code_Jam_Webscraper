from heapq import heappush, heappop
t=int(input())
for testcase in range(t):
  n,k=map(int,input().split())
  heap=[]
  heappush(heap,-n)
  l=0
  r=0
  for i in range(k):
    top=heappop(heap)*-1
    l=int((top-1)/2)
    r=top-1-l
    heappush(heap,-l)
    heappush(heap,-r)
  print("Case #"+str(testcase+1)+": "+str(r)+" "+str(l))
  