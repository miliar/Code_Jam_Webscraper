def main():
  T = int(raw_input())
  for case in xrange(T):
    N = int(raw_input())
    m = [int(x) for x in raw_input().split()]
    one = 0
    two = 0
    biggest = 0
    for i in xrange(N-1):
      if m[i] - m[i+1] > 0:
        one += m[i] - m[i+1]
      if m[i] - m[i+1] > biggest:
        biggest = m[i] - m[i+1]
    for i in xrange(N-1):
      if m[i] >= biggest:
        two += biggest
      else:
        two += m[i]
        """
      if m[i] - m[i+1] < 0:
        two += m[i+1]
      else:
        two += biggest
        """
    print "Case #%d: %d %d" % (case+1, one, two)

if __name__ == "__main__":
  main()
