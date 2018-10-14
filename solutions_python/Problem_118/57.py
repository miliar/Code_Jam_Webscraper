d = [0] * 25
all = []

def rev(n):
  r = 0;
  while (n > 0):
    r = r * 10 + (n % 10)
    n //= 10
  return r

def go(idx, n, s, last):
  if idx > 0:
    if s+s-last*last < 10:
      res = 0
      for i in xrange(idx):
        res = res * 10 + d[i]
      for i in xrange(idx-2, -1, -1):
        res = res * 10 + d[i]
      all.append(res*res)

    if s+s < 10:
      res = 0
      for i in xrange(idx):
        res = res * 10 + d[i]
      for i in xrange(idx-1, -1, -1):
        res = res * 10 + d[i]
      all.append(res*res)

  if idx == n: return
  i = 0
  if idx == 0: i = 1
  while True:
    if s+s+i*i >= 10: break
    d[idx] = i
    go(idx+1, n, s+i*i, i)
    i += 1

go(0, 25, 0, 0)

all = sorted(all)

cases = int(raw_input())
for caseNo in xrange(1, cases+1):
  ss = raw_input().split()
  a = int(ss[0])
  b = int(ss[1])
  res = 0
  for x in all:
    if a <= x and x <= b: res += 1
    if x > b: break
  print "Case #%d: %d" % (caseNo, res)

