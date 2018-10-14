def test(i):
  T = [x for x in L[:i+1]]
  T.sort()
  for i in range(len(T)):
    if T[i] > i:
      return False
  return True

f = open('p1.in', 'r')
T = int(f.readline())
for x in range(T):
  n = int(f.readline())
  A = [f.readline()[:-1] for i in range(n)]
  L = []
  j = 0
  sol = 0
  for s in A:
    L.append(-1)
    for i in range(n):
      if s[i] == '1':
        L[-1] = i
  for i in range(n-1, 0, -1):
    if test(i-1):
      continue
    for j in range(i-1, -1, -1):
      aux = L[j]
      L[j] = L[i]
      if test(i-1):
        L[j] = aux
        break
      L[j] = aux
    sol += i - j
    for ii in range(j, i):
      L[ii] = L[ii + 1]
  print 'Case #%s: %s' % (x + 1, sol)
