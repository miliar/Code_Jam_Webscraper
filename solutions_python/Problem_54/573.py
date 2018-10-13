def cmmdc(i, j):
  if i < 0:
    i = -i
  if j < 0:
    j = -j
  while i and j:
    if i >= j:
      i %= j
    else:
      j %= i
  return i | j

f = open('b.in', 'r')
T = int(f.readline())
for ii in range(T):
  A = [int(x) for x in f.readline().split(' ')]
  n = A[0]
  A = A[1:]
  N = 0
  for i in A:
    for j in A:
      N = cmmdc(N, i - j)
  if A[0] % N == 0:
    print 'Case #%s: %s' % (ii + 1, 0)
  else:
    print 'Case #%s: %s' % (ii + 1, N - (A[0] % N))
