if __name__ == '__main__':
  tc = int(raw_input())
  for cc in range(1, tc + 1):
    n, p = [int(x) for x in raw_input().split()]
    g = [int(x) for x in raw_input().split()]
    if p == 2:
      print "Case #%d: %d" % (cc, n - len([x for x in g if x % 2 == 1]) // 2)
    else:
      n1 = len([x for x in g if x % 3 == 1])
      n2 = len([x for x in g if x % 3 == 2])
      r = min(n1, n2)
      r += len([x for x in range(n1 - min(n1, n2)) if x % 3 != 0])
      r += len([x for x in range(n2 - min(n1, n2)) if x % 3 == 1])
      r += len([x for x in range(n2 - min(n1, n2)) if x % 3 == 2])
      print "Case #%d: %d" % (cc, n - r)
