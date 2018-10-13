

ncases = int(input())
for caseno in range(1, ncases+1):
  ndiscs, cap = map(int, input().split())
  sizes = list(map(int, input().split()))
  sizes.sort()

  n = 0
  i, j = 0, ndiscs-1
  while i <= j:
    d = sizes[j]
    j -= 1
    if i <= j:
      if sizes[i] + d <= cap:
        i += 1
    n += 1
  
  print('Case #%d: %d' % (caseno, n))
