nb_tc = input()

for itc in xrange(nb_tc):
  N,M = [int(x) for x in raw_input().split(' ')]
  a,mN,mM=[],[],[]
  for i in range(N):
    a.append(raw_input().split(' '))
    mN.append(a[i][0])
  for i in range(M):
    mM.append(a[0][i])
  for i in range(N):
    for j in range(M):
      if a[i][j] > mM[j]:
        mM[j]=a[i][j]
      if a[i][j] > mN[i]:
        mN[i]=a[i][j]
  ok = True
  for i in range(N):
    for j in range(M):
      if a[i][j] != mM[j] and a[i][j] != mN[i]:
        ok = False
  if ok:
    print "Case #%d: YES" % (itc+1)
  else:
    print "Case #%d: NO" % (itc+1)
