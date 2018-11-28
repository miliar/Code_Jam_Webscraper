T = int(raw_input())

d0 = {}
d1 = {}

def dev(a, b, c):
  ab = abs(a - b)
  ac = abs(a - c)
  bc = abs(b - c)
  return max(ab, ac, bc)

for i in range(31):
  for j in range(31):
    for k in range(31):
      s = i + j + k
      if dev(i, j, k) <= 1:
        d0.setdefault(s, 0)
        d0[s] = max(d0[s], max(i, j, k))
      elif dev(i, j, k) <= 2:
        d1.setdefault(s, 0)
        d1[s] = max(d1[s], max(i, j, k))
        
for Ca in xrange(1, T + 1):
  print 'Case #{}:'.format(Ca),
  l = map(int, raw_input().strip().split(' '))
  N, S, P, l = l[0], l[1], l[2], l[3:]

  ans = 0
  for li in l:
    if li in d0 and d0[li] >= P:
      ans += 1
    elif li in d1 and d1[li] >= P and S >= 1:
      S -= 1
      ans += 1

  print ans
