T=int(input())
for i in range(T):
  N=int(input())
  li=[int(x) for x in input().split()]
  fp=len([i for i in range(N) if i+1==li[i]])
  ans=N-fp
  print('Case #%d: %f' % (i+1,ans))
