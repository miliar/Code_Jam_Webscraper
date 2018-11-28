T=int(input())
for i in range(T):
  N=int(input())
  li=[int(x) for x in input().split()]
  total=0
  for y in li:
    total=total^y
  if total==0:
    ans = sum(li)-min(li)
    print('Case #%d: %d' % (i+1,ans))
  else:
    print('Case #%d: NO' % (i+1))