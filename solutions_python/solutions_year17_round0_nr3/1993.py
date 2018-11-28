import heapq

def check(N,K):
  h = []
  heapq.heappush(h,-N)
  for i in range(K-1):
    a = heapq.heappop(h)
    if a >= -1:
      return [0, 0]
    a1 = (a+1)//2
    a2 = a+1-a1
    heapq.heappush(h,a1)
    heapq.heappush(h,a2)
  a = heapq.heappop(h)
  if a >= -1:
    return [0, 0]
  a1 = (a+1)//2
  a2 = a+1-a1
  return [-a1,-a2]

T = int(input())
for i in range(1,T+1):
  N, K = map(int, input().split())
  ans = check(N, K)
  print('Case #{}: {} {}'.format(i,ans[0],ans[1]))
