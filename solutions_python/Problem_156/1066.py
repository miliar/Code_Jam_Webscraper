import sys

def stuff(indexdata, curm):
  m = curm
  while m > 0 and indexdata[m] == 0:
    m -= 1

  if m == 1:
    return 1
  if m <= 0:
    return 0

  n = indexdata[m]
  indexdata[m] = 0
  t = m
  top = (m / 2) if m % 2 == 0 else (m / 2 + 1)
  for x in xrange(1, top + 1):
    indexdata[x] += n
    indexdata[m - x] += n
    other = n + stuff(indexdata, m - 1)
    if t > other:
      t = other
    indexdata[x] -= n
    indexdata[m - x] -= n

  indexdata[m] = n

  return t

def main():
  cases = int(sys.stdin.readline())
  for case in xrange(cases):
    n = int(sys.stdin.readline())
    data = [int(k) for k in sys.stdin.readline().split(' ')]
    indexdata = {}
    for i in xrange(max(data) + 1):
      indexdata[i] = 0

    for d in data:
      indexdata[d] += 1

    #print(data)
    t = stuff(indexdata, max(data))

    print("Case #%d: %d" % (case + 1, t))

main()

