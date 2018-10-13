def get(a, b):
  s = a[0] * b[0]
  a, b = a[1], b[1]
  if a == 1:
    r = b
  elif a == b:
    r = 1
    s *= -1
  elif b == 1:
    r = a
  elif a == 'i':
    if b == 'j':
      r = 'k'
    else:
      r = 'j'
      s *= -1
  elif a == 'j':
    if b == 'i':
      r = 'k'
      s *= -1
    else:
      r = 'i'
  else:
    if b == 'i':
      r = 'j'
    else:
      r = 'i'
      s *= -1
  return (s, r)

def getans(t):
  if t[-1] != (-1, 1):
    return False
  for i in xrange(len(t)):
    if t[i] != (1, 'i'):
      continue
    for j in xrange(i + 1, len(t)):
      if t[j] != (1, 'k'):
        continue
      return True
  return False

def solve(tcase):
  L, X = raw_input('').split()
  L, X = int(L), int(X)
  s = raw_input('')
  s *= X
  t = [(1, s[0])]
  for i in xrange(1, len(s)):
    t.append(get(t[-1], (1, s[i])))
  #print s
  #print t
  print 'Case #%d: %s' % (tcase, 'YES' if getans(t) else 'NO')

T = int(raw_input(''))
for tcase in xrange(1, T + 1):
  solve(tcase)