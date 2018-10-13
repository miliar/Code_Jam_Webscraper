nt = int(input())
for tt in range(nt):
  a = list(input().split()[1:])
  n = len(a) // 2
  po = pb = 1
  to = tb = 0
  res = 0
  for i in range(n):
    t = int(a[i * 2 + 1])
    if a[i * 2] == 'O':
      d = abs(po - t)
      z = max(0, d - (res - to))
      res += z + 1
      to = res
      po = t
    else:
      d = abs(pb - t)
      z = max(0, d - (res - tb))
      res += z + 1
      tb = res
      pb = t
  print('Case #' + str(tt + 1) + ': ' + str(res))
