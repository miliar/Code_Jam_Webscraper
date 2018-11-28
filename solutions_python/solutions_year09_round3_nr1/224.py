import math

def base_to_decimal(num, base):
  out = 0
  exp = 0
  i = len(num) - 1
  while i >= 0:
    out += (int(num[i]) * int(math.pow(base, exp)))
    #print 'out=', out
    exp += 1
    i -= 1
  return str(out)

C = int(raw_input())
for _c in xrange(C):
  s = raw_input()
  #print s
  s_set = set(s)
  base = len(s_set)
  if base == 1: base = 2
  #print base
  m = {}
  m[s[0]] = '1'
  i = 0
  for c in s:
    if c not in m:
      m[c] = str(i)
      i += 1
      if i == 1:
        i += 1
        
  out = ''
  for c in s:
    out += m[c]
    
  #print out
  
  print 'Case #' + str(_c+1) + ':', base_to_decimal(out, base)
