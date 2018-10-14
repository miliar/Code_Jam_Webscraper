import heapq
f = open('C-small-2-attempt2.in', 'r')
ff=open('C-small-2-attempt2.out', 'w')
t = int(f.readline())
for i in range(t):
  n,k = f.readline().split(' ')
  n=int(n)
  k=int(k)
  x=[]
  heapq.heapify(x)
  heapq.heappush(x, (-n, (0,n)))
  for j in range(k - 1):
    v,(l,r) = heapq.heappop(x)
    mid = (l+r)//2
    if mid > l:
      heapq.heappush(x, (-(mid-l), (l,mid)))
    if r > mid+1:
      heapq.heappush(x, (-(r-mid-1), (mid+1, r)))
  v,(l,r) = heapq.heappop(x)
  # print(l, r)
  # print(x)
  mid=(l+r)//2
  ff.write('Case #' + str(i+1) + ': ')
  ff.write(str(max(mid-l, r-mid-1)))
  ff.write(' ')
  ff.write(str(min(mid-l, r-mid-1)))
  ff.write('\n')
