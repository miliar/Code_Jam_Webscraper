ri = raw_input

def solve(str):
  tinp = str.split()
  mates = {}
  enemies = {}
  C = int(tinp[0])
  for i in xrange(1, C+1):
    a, b, c = tinp[i]
    mates[(a, b)] = mates[(b, a)] = c
  D = int(tinp[C+1])
  for i in tinp[C+2:-2]:
    a, b = i
    if a in enemies:
      enemies[a].add(b)
    else:
      enemies[a] = set(b)
    a, b = b, a
    if a in enemies:
      enemies[a].add(b)
    else:
      enemies[a] = set(b)
  s = tinp[-1]
  l = []
  #print
  for e in s:
    l.append(e)
    if len(l) > 1:
      a, b = l[-2:]
      if (a, b) in mates:
        #print ' ', l, (a, b), mates[(a, b)]  
        l.pop(); l.pop(); l.append(mates[(a, b)])
        #print ' ', l
      else:
        if e in enemies:
          for E in enemies[e]:
            if E in l:
              l = []
              break
  return repr(l).replace("'", '')





n = int(ri())
for i in xrange(1,n+1):
  print "Case #%d:"%i, solve(ri())
  