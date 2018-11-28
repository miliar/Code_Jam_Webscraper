def flip(s, k, pos):
  for i in xrange(pos, pos+k):
    if s[i] == '+':
      s[i] = '-'
    else:
      s[i] = '+'
  return s

def solve(s, k):
  res = 0
  for i in xrange(len(s) - k + 1):
    if s[i] == '-':
      flip(s, k, i)
      res += 1
  if '-' in s:
    return 'IMPOSSIBLE'
  return res

t = int(raw_input())
for i in xrange(1, t + 1):
  s, k = [c for c in raw_input().split(" ")]  
  s = list(s)
  k = int(k)
  print "Case #{}: {}".format(i, solve(s, k))