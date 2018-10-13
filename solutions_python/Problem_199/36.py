t = int(input())

for ti in range(1,t+1):
  s,m = input().split()
  a = [c == '+' for c in s]
  m = int(m)
  ans = 0
  for i in range(len(a)-m+1):
    if a[i]: continue
    ans += 1
    for j in range(m):
      a[i+j] = not a[i+j]
  for x in a:
    if not x: ans = 'IMPOSSIBLE'
  print('Case #{}: {}'.format(ti,ans))
