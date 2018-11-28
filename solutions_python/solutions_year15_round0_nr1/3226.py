from sys import stdin

cases = stdin.read().splitlines()[1 :]
for i, case in enumerate(cases, 1):
  S = [int(x) for x in case.split()[1]]
  a = 0
  x = 0
  for j, y in enumerate(S):
    if x < j:
      a += j - x
      x += j - x
    x += y

  print('Case #%d:' % i, a)
