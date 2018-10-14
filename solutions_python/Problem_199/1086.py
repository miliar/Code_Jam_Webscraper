for t in range(input()):
  s, k = raw_input().split()
  k, n, a = int(k), len(s), map(lambda x: x=='+', s)
  ans = 0
  for i in range(n):
    if a[i]: continue
    if i+k > n:
      ans = 'IMPOSSIBLE'
      break
    ans += 1
    for j in range(i, i+k): a[j] = not a[j]
  print('Case #%d: %s' % (t+1, ans))
