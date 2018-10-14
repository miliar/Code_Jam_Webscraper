import sys

def flip_n(arr):
  return [flip(c) for c in arr]

def flip(c):
  if c == '+':
    return '-'
  if c == '-':
    return '+'
  raise Exception('oops')

def flips(row, k):
  curr = 0
  s = list(row)
  flipped = 0
  while curr >= 0 and curr < len(s):
    if s[curr] == '+':
      curr += 1
      continue
    else:
      if curr + k > len(s):
        return "IMPOSSIBLE"
      s[curr:curr+k] = flip_n(s[curr:curr+k])
      flipped += 1
  if any(c == '-' for c in s):
    return "IMPOSSIB:E"
  return flipped


ct = 0
for line in sys.stdin:
  ct += 1
  if ct == 1:
    continue
  parts = line.split(' ')
  row = parts[0]
  k = int(parts[1])
  print("Case #{0}: {1}".format(ct-1, flips(row, k)))

