T = int(input())
for t in range(T):
  n, k = map(int, input().split())
  u = float(input())
  p = sorted(map(float, input().split()))
  cur = 0
  for i, v in enumerate(p):
    if i*(v-cur) <= u:
      u -= i*(v-cur)
      cur = v
    else:
      cur += u/i
      break
  else:
    cur += u/n

  res = 1
  for v in p:
    res *= max(v, cur)
  print("Case #"+str(t+1)+":", res)
  