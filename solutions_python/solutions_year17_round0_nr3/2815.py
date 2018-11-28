def printOut(I, p1, p2):
  print "Case #{}: {} {}".format(I, p1, p2)

def bathroomStall(N, K):
  bs = [1] + [0]*N + [1];

  for person in xrange(1, K+1):
    #print ""
    #print "PERSON", person
    pos = 0
    while bs[pos]==1:
      pos += 1

    #print "pos", pos

    ls = leftStalls(pos, bs)
    rs = rightStalls(pos, bs)

    #print "leftstalls", ls
    #print "rightstalls", rs

    # calc min_lsrs
    min_lsrs = [min(ls,rs)]
    min_ls = [ls]
    min_rs = [rs]
    min_p = [pos]
    for p in xrange(pos, N+1):
      #print "p", p
      if bs[p]==1:
        continue

      ls = leftStalls(p, bs)
      rs = rightStalls(p, bs)

      if min_lsrs[0] < min(ls,rs):
        #print "set min_lsrs"
        min_lsrs = [min(ls,rs)]
        min_ls = [ls]
        min_rs = [rs]
        min_p = [p]

      #print "min_lsrs", min_lsrs, "min(ls,rs)", min(ls,rs)
      if min_lsrs[0] == min(ls,rs):
        min_lsrs.append(min(ls,rs))
        min_ls.append(ls)
        min_rs.append(rs)
        min_p.append(p)

    #print "min_lsrs", min_lsrs
    #print "min_ls", min_ls
    #print "min_rs", min_rs
    #print "min_p", min_p

    # calc max_lsrs
    max_lsrs = max(min_ls[0], min_rs[0])
    max_p = min_p[0]
    #print "max_lsrs", max_lsrs
    #print "max_p", max_p
    for i in xrange(0, len(min_lsrs)):
      if max_lsrs < max(min_ls[i], min_rs[i]):
        max_lsrs = max(min_ls[i], min_rs[i])
        max_p = min_p[i]

    bs[max_p] = 1

  return [max_lsrs, min_lsrs[0]]

def leftStalls(p, bs):
  ls = 0
  while p-1 > 0 and not bs[p-1]:
    ls += 1
    p -= 1
  return ls

def rightStalls(p, bs):
  rs = 0
  while p+1 < len(bs) and not bs[p+1]:
    rs += 1
    p += 1
  return rs

#print bathroomStall(4, 2)

t = int(raw_input())
for I in xrange(1, t + 1):
  N, K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  
  mx, mn = bathroomStall(N, K)
  printOut(I, mx, mn)


  #mx, mn = bathroomStall(N, K)
  ##printOut(I, )

  ##printOut(I, 2*n, 2*m);


