def minNumberIndexInListGreaterThan(ls, num):
  l = ls[:]
  l.sort()
  for i, x in enumerate(l):
    if x > num:
      return i
  return None

fi = open('D-large.in','r')
t = int(fi.readline())
for i in xrange(0, t):
  n = int(fi.readline())
  blocksNaomi = map(float, fi.readline().split())
  blocksKen = map(float, fi.readline().split())

  point = 0
  opt_point = 0

  # Normal
  bn = blocksNaomi[:]
  bk = blocksKen[:]
  bn.sort()
  bk.sort()
  for j in xrange(0, n):
    naomi = bn.pop(0)
    index = minNumberIndexInListGreaterThan(bk, naomi)
    if index != None:
      ken = bk.pop(index)
    else:
      ken = bk.pop(0)
    if naomi > ken:
      point += 1
  
  # Deceitful
  bn = blocksNaomi[:]
  bk = blocksKen[:]
  bn.sort()
  bk.sort()
  for j in xrange(0, n):
    naomi = bn.pop(0)      
    if naomi > max(bk):
      # Naomi cannot deceit
      ken = bk.pop()
    else:
      if naomi < min(bk):
        # Naomi never wins so makes him to use the heviest block
        ken = bk.pop()
      else:
        ken = bk.pop(0)
    if naomi > ken:
      opt_point += 1
  print "Case #%d: %d %d" % (i+1, opt_point, point)
fi.close
