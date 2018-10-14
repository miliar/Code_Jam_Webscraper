import sys, shlex, math

def count_combs(n, B):
  count = nbrot = 0
  goods = []
  while True:
    m = str(n)
    for i in xrange(nbrot):
      m = m[-1:]+m[:-1]
    nbrot += 1
    if nbrot > len(m):
      break
    if m not in goods:
      if ((len(m)) == len(str(n)) and int(m) > n and int(m) <= B) == True:
        goods.append(m)
        count += 1
  return count

def compute_n(A, B):
  count = 0
  n = A
  if ((len(str(A)) == len(str(B))) and A > 1):
    while (n <= B):
      count += count_combs(n, B)
      n += 1
  return count

def count_rnums(line):
  params = shlex.split(line)
  A = int(params[0])
  B = int(params[1])
  return compute_n(A, B)

nblines = sys.stdin.readline()
for i in xrange(int(nblines)):
  line = sys.stdin.readline()
  resline = count_rnums(line.rstrip('\r\n'))
  print "Case #%s: %s" % ((i + 1), resline)