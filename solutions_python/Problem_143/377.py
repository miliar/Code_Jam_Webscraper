def main():
  f = open('B.in', 'r')
  T = int (f.readline())

  for t in range(1, T+1):
    print 'Case #' + str(t) + ':',
    A, B, K = map(int, f.readline().split())
    c = 0
    for a in range(A):
      for b in range(B):
        if (a & b < K):
          c += 1
    print c

if __name__ == "__main__":
    main()
