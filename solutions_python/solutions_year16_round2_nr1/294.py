n=input()

def compute(s, idx, res):
  #print s, idx, res
  digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
  if idx >= len(digits):
    return False
  tmps = list(s)
  digit = digits[idx]
  found = True
  for d in digit:
    try:
      a=tmps.index(d)
      del(tmps[a])
    except:
      found = False

  if found and len(tmps) == 0:
    print ''.join(map(str, res+[idx]))
    return True
  elif not found:
    return compute(s, idx + 1, res)
  else:
    s2 = ''.join(tmps)
    return compute(s2, idx, res + [idx]) or compute(s2, idx + 1, res + [idx]) or compute(s, idx + 1, res)

for x in xrange(n):
  m = raw_input()
  print 'Case #'+str(x+1)+':',
  compute(m, 0, [])