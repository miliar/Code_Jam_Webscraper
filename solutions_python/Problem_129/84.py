def cost(f, t, n):
  cnt = t-f
  return ((cnt*n) - (cnt*(cnt-1)//2))

mod = 1000002013

T = int(input())+1

for t in range(1, T):
  N, M = map(int, input().split())
  osum, nsum = 0, 0
  pnt, stack = [], []
  for i in range(M):
    beg, end, p = map(int, input().split())
    osum += p*cost(beg, end, N)
    pnt.append((beg, -p))
    pnt.append((end, p))
  pnt.sort()
  index = 0
  for x in pnt:
    index += 1
    if x[1] > 0:
      #while nevystupilo dost
      ac = (0, 0)
      out = 0
      while out < x[1]:
        if ac[1] == 0: ac = stack.pop()
        tt = min(ac[1], x[1]-out)
        nsum += tt*cost(ac[0], x[0], N)
        out += tt
        ac = (ac[0], ac[1]-tt)
      if ac[1] > 0: stack.append(ac)
    else:
      stack.append((x[0], -x[1]))
  print("Case #" + str(t) + ": " + str((osum-nsum)%mod))
