f = open('a.in', 'r')
T = int(f.readline())
for ii in range(T):
  n, k = [int(x) for x in f.readline().split(' ')]
  aux = True
  for i in range(n):
    if not (k & (1 << i)):
      aux = False
  if aux:
    print 'Case #%s: ON' % (ii + 1)
  else:
    print 'Case #%s: OFF' % (ii + 1)
