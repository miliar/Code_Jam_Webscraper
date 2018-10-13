fname = "C-large.in"
# fname = "testc.in"

head = ["1", "i", "j", "k", "-1", "-i", "-j", "-k"]
M = [
      ["1", "i", "j", "k", "-1", "-i", "-j", "-k"],
      ["i", "-1", "k", "-j", "-i", "1", "-k", "j"],
      ["j", "-k", "-1", "i", "-j", "k", "1", "-i"],
      ["k", "j", "-i", "-1", "-k", "-j", "i", "1"],
      ["-1", "-i", "-j", "-k", "1", "i", "j", "k"],
      ["-i", "1", "-k", "j", "i", "-1", "k", "-j"],
      ["-j", "k", "1", "-i", "j", "-k", "-1", "i"],
      ["-k", "-j", "i", "1", "k", "j", "-i", "-1"]
    ]

def resolve(x, y):
  return M[head.index(x)][head.index(y)]

def resolves(st):
  l = len(st)
  res = "1"
  for i in xrange(0, l):
    res = resolve(res, st[i])
    # print res
  return res

def find(bigst, letter):
  current = "1"
  while True:
    latest = bigst.pop(0)
    value = resolve(current, latest)
    if value == letter:
      return bigst
    if len(bigst) == 0:
      return False
    current = value

def solve_k(st, X, pre, totals):
  # print st, X, pre
  if type(pre) is list:
    pre.append(totals[X % 4])
    return resolves(pre) == "k"
  else:
    return resolve(pre, totals[X % 4]) == "k"

def solve_j(st, X, pre, prefixes, totals):
  # print st, X, pre
  # print prefixes, totals

  nprefixes = [pre[0]]
  for i in xrange(1, len(pre)):
    nprf = resolve(nprefixes[-1], pre[i])
    nprefixes.append(nprf)
  
  # print nprefixes

  if "j" in nprefixes:
    ind = nprefixes.index("j")
    return solve_k(st, X, pre[(ind+1):], totals)
  else:
    if X == 0:
      return False
    tot = nprefixes[-1]
    # print tot
    for i in xrange(4):
      pre = totals[i]
      for j in xrange(len(prefixes)):
        # print "A", resolve(pre, prefixes[j])
        res = resolve(tot, resolve(pre, prefixes[j]))
        # print res
        if res == "j":
          # print j
          if j == 0:
            return solve_k(st, X-i, "1", totals)
          # we've found it!
          else:
            return solve_k(st, X-i-1, st[j:], totals)
    return False
    # newprefixes = [resolve(tot, p) for p in prefixes]
    # if "j" in newprefixes:
    #   ind = newprefixes.index("j")
    #   if ind == len(st) - 1:
    #     return solve_k(st, X-1, "1", totals)
    #   return solve_k(st, X-1, st[(ind+1):], totals)


def solve(st, X):
  # print st, X
  # create prefixes
  prefixes = ["1"]
  for i in xrange(0, len(st)):
    prefix = resolve(prefixes[-1], st[i])
    prefixes.append(prefix)

  # print prefixes

  # calculate all permutations of the middle section
  total = prefixes.pop()
  totals = ["1"]
  newtotal = "1"
  for i in xrange(3):
    newtotal = resolve(newtotal, total)
    totals.append(newtotal)

  # print totals

  for i in xrange(4):
    pre = totals[i]
    for j in xrange(len(prefixes)):
      res = resolve(pre, prefixes[j])
      if res == "i":
        if j == 0:
          return solve_j(st, X-i, "1", prefixes, totals)
        # we've found it!
        else:
          return solve_j(st, X-i-1, st[j:], prefixes, totals)
  return False


def main():
  with open(fname) as f:
    for i in xrange(int(f.readline())):
      L, X = map(int, f.readline().split())
      st = list(f.readline().rstrip())
      print 'Case #%s: %s' % (i + 1, "YES" if solve(st, X) else "NO")

main()