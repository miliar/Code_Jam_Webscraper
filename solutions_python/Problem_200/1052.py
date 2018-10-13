def tidy(n):
  ns = [c for c in str(n)]
  prev = ns[0]
  for i in ns[1:]:
    if prev > i:
      return False
  return True

def fix(n, ns):
  prev = ns[0]
  dom = 0
  fail = False
  for idx, i in enumerate(ns[1:]):
    if prev < i:
      dom = idx + 1
    elif prev == i:
      pass
    elif prev > i:
      fail = True
      break
    prev = i
  if fail:
    ns[dom] = str(int(ns[dom]) - 1)
    for idx in xrange(dom + 1, len(ns)):
      ns[idx] = '9'
    return int(''.join(ns))
  else:
    return n

t = int(raw_input())
for i in xrange(1, t + 1):
  num = int(raw_input())
  ns = [c for c in str(num)]
  f = fix(num, ns)	
  print "Case #{}: {}".format(i, f)
