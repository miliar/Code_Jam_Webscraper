import sys

def check(pattern, char='+'):
  for c in pattern:
    if c != char:
      return False
  return True

def flip(pattern, num):
  if num <= 1:
    return pattern
  for i in range(1, num):
    if pattern[i] == '+':
      pattern[i] = '-'
    else:
      pattern[i] = '+'
  return pattern

def get_flips(pattern, num):
  if check(pattern):
    return 0
  if len(pattern) < num:
    return sys.maxsize
  if len(pattern) == num:
    if check(pattern, '-'):
      return 1
    return sys.maxsize

  if pattern[0] == '+':
    return get_flips(pattern[1:], num)
  pattern = flip(pattern, num)
  flips = get_flips(pattern[1:], num)
  if flips == sys.maxsize:
    return sys.maxsize
  return 1 + flips

t = int(raw_input())
for i in xrange(1, t + 1):
  n, m = [s for s in raw_input().split(" ")]
  flips = get_flips(list(n), int(m))
  if flips == sys.maxsize:
    print ("Case #{}: IMPOSSIBLE".format(i))
  else:
    print ("Case #{}: {}".format(i, flips))

