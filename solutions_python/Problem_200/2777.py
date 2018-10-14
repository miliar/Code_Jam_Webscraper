import sys

def to_list(n):
  l = []
  for c in str(n):
    l.append(int(c))
  return l

def to_num(n):
  tot = 0
  for i in xrange(0, len(n)):
    tot += 10**i * n[len(n)-1-i]
  return tot

def prev_tidy(n):
  x = to_list(n)
  curr = 1
  right = True
  while curr >= 0 and curr < len(x):
    if right:
      if x[curr] < x[curr-1]:
        x[curr:] = [9] * (len(x) - curr)
        x[curr-1] -= 1
        right = False
        continue
      curr += 1
    else:
      if curr - 1 >= 0 and x[curr-1] > x[curr]:
        x[curr] = 9
        x[curr-1] -= 1
      curr -= 1
  return to_num(x)
ct = 0
for line in sys.stdin:
  ct += 1
  if ct == 1:
    continue
  print("Case #{0}: {1}".format(ct-1, prev_tidy(int(line))))

