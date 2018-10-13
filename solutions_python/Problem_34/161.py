f = open('a.in', 'r')
buf = f.readline()
l, d, n = [int(x) for x in buf.split(' ')]
W = []
for x in range(d):
  W.append(f.readline()[:l])
for tno in range(1, n + 1):
  w = f.readline()[:-1]
  sol = d
  for j in range(d):
    i = 0
    for idx in range(l):
      if w[i] == '(':
        s = set()
        i += 1
        while w[i] != ')':
          s.add(w[i])
          i += 1
      else:
        s = set([w[i]])
      if W[j][idx] not in s:
        sol -= 1
        break
      i += 1
  print 'Case #%s: %s' % (tno, sol)
