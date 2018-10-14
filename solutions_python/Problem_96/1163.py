import sys

p = sys.argv[1]
f = open(p)
n = int(f.readline())

# if score is >= 3p - 2, guaranteed
# if score is 3p-3 or 3p-4, could be
# if score is less than 3p-4, can't be
def compute(n, s, p, ts):
  toolow = 0
  guaranteed = 0
  maybe = 0

  gn = 3*p - 2
  ln = max(3*p - 4, p)

  #print p, s, gn, ln
  #print n, s, p, ts
  for t in ts:
    if t >= gn:
      guaranteed += 1
    elif t < ln:
      toolow += 1
    else:
      maybe += 1
  return guaranteed + min(maybe, s)

for l in range(n):
  nums = [int(x) for x in f.readline().split(' ')]
  np = compute(nums[0], nums[1], nums[2], nums[3:])
  print "Case #%s: %s" % (l + 1, np)


