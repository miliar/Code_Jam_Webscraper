def calc(c, f, x):
  # I wish I knew more calculus
  best = x / 2.0
  cand = c / 2.0 + x / (f + 2.0)
  i = 1
  while cand < best:
    best = cand
    k = (i*f + 2.0)
    cand = cand - x / k + c / k + x / (k+f)
    i += 1
  return best

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1 and sys.argv[1] == 'tests':
    assert 526.190 < calc(500.0, 4.0, 2000.0) < 526.191
    assert 39.1666 < calc(30.0, 2.0, 100.0) < 39.16667
    assert 0.999999 < calc(30.0, 1.0, 2.0) < 1.00001
    assert 63.9680 < calc(30.50, 3.14159, 1999.1999) < 63.9681
  else:
    for t in range(int(raw_input())):
      c, f, x = map(float, raw_input().split())
      print 'Case #%d: %.7f' % (t+1, calc(c, f, x))
