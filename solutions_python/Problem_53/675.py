def snapper(n, snaps):
  v = pow(2, n)
  s = snaps % v
  if s == (v - 1):
    return "ON"
  return "OFF"


if __name__ == "__main__":
  # f = open("A-test.in")
  # f = open("A-small.in")
  f = open("A-large.in")
  T = int(f.readline().strip())
  for i in range(0, T):
     (N, K) = f.readline().strip().split(' ')
     print "Case #%d: %s" % (i + 1, snapper(int(N), int(K)))
