if __name__ == '__main__':
  t = int(raw_input())
  for _t in xrange(t):
    smax, inp = raw_input().split(' ')
    inp = map(int, list(inp))
    total, extra = 0, 0
    for ind, i in enumerate(inp):
      if ind > total:
        diff = ind - total
        extra += diff
        total += diff
      total += i

    print ''.join(['Case #', str(_t+1), ': ', str(extra)])
