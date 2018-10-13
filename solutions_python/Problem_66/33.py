def solve(P, M, tree):
  INF = 1 << 31
  D = {}
  i = len(tree) - 1
  while i >= 0:
    # If leaf...
    if i << 1 >= (1 << P) - 2:
      must = M[i - (1 << (P-1)) + 1]
      for bup in xrange(0, P+1):
        if bup >= must:
          D[(i, bup)] = 0
        elif bup + 1 == must:
          D[(i, bup)] = tree[i]
    else:
      left = i << 1 | 1
      right = left + 1
      for bup in xrange(0, P+1):
        result = INF
        if (left, bup) in D and (right, bup) in D:
          result = min(result, D[(left, bup)] + D[(right, bup)])
        if (left, bup+1) in D and (right, bup+1) in D:
          result = min(result, D[(left, bup+1)] + D[(right, bup+1)] + tree[i])
        if result < INF:
          D[(i, bup)] = result

    i -= 1

  return D[(0, 0)]

def read(f):
  P = int(f.readline().strip())
  M = [0] * (1 << (P-1))
  strarr = f.readline().strip().split()
  for i in xrange(1 << P):
    k = P - int(strarr[i])
    M[i >> 1] = max(M[i >> 1], k)
  tree = [0] * ((1 << P) - 1)
  for i in xrange(P-1, -1, -1):
    strarr = f.readline().strip().split()
    for j in xrange(len(strarr)):
      tree[(1 << i) + j - 1] = int(strarr[j])
  return P, M, tree

def main():
  FILENAME = 'world'
  f = open('%s.in' % FILENAME, 'r')
  g = open('%s.out' % FILENAME, 'w')

  T = int(f.readline().strip())

  for t in xrange(1, T+1):
    data = read(f)
    result = solve(*data)

    # Print testcase.
    g.write('Case #%s: %s\n' % (t, result))

  f.close()
  g.close()

if __name__ == '__main__':
  main()
  print 'Done.'
