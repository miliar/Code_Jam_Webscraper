

def is_tidy(n):
  s = str(n)
  for i, c in enumerate(s):
    if i == 0:
      continue
    if s[i-1] > c:
      return False
  return True

def solve(n):
  for i in xrange(n, 0, -1):
    if is_tidy(i):
      return i

if __name__ == "__main__":
  T = int(raw_input())
  for t in xrange(1, T+1):
    n = int(raw_input())
    print "Case #%d: %d" % (t, solve(n))