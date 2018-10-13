
for case in range(1, int(input()) + 1):
  s = [int(n) for n in input().split()]
  L, t, N, C = s[:4]
  a = [2*i for i in s[4:4+C]]

  stars = []
  while True:
    if len(stars) == N:
      break
    for star in a:
      if len(stars) == N:
        break
      stars.append(star)

  hours = 0
  while t and len(stars):
    if stars[0] <= t:
      t -= stars[0]
      hours += stars.pop(0)
    else:
      stars[0] -= t
      hours += t
      t = 0

  for i in sorted(stars, reverse=True):
    if L:
      hours += i / 2
      L -= 1
    else:
      hours += i

  print('Case #%d: %d' % (case, hours))
