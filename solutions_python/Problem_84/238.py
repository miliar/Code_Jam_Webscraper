import sys

def doit():
  for r in rows:
    if rows[r].count('#')%2 != 0:
      return False
  for c in cols:
    if cols[c].count('#')%2 != 0:
      return False
  return True

i = sys.stdin
n = int(i.readline())

for _n in xrange(1,n+1):
  h,w = map(int,i.readline().split())
  rows = {}
  cols = {}
  OK = True
  red = ["/\\","\/"]
  for x in xrange(h):
    c = i.readline().strip()
    rows[x] = c
    for y in xrange(w):
      if y in cols:
        cols[y] += c[y]
      else:
        cols[y] = c[y]

  print "Case #%i:"%_n
  possible = doit()
  if possible:
    rl = "0"*w
    cl = 0
    for r in rows:
      l = rows[r]
      while "#" in l:
        a= l.index("#")
#l[a] = red[int(rl[a])][cl]
        l = l.replace("#",red[int(rl[a])][cl],1)
        cl^=1
        rl_l = list(rl)
        rl_l[a] = str(int(rl[a])^1)
        rl = "".join(rl_l)
      print l
  else:
    print "Impossible"



