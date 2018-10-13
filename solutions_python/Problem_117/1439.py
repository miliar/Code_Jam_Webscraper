#!/usr/bin/env python2
import sys
import io

def main():
  s = sys.stdin.read().split()

  T = int(s[0])
  s = s[1:]

  for t in range(T):
    N = int(s[0])
    M = int(s[1])
    matrix = []
    for n in range(N):
      matrix.append([])
      for m in range(M):
        matrix[-1].append(int(s[2 + n * M + m]))

    s = s[2 + N * M:]
    rows = []
    cols = []
    for line in matrix:
      rows.append(line == [1] * len(line))

    for m in range(M):
      cols.append(map(lambda X: matrix[X][m], range(N)) == [1] * N)

    good = True
    for i in range(N):
      for j in range(M):
        if matrix[i][j] == 1 and not (rows[i] or cols[j]):
          good = False

    print "Case #%d: %s" % (t + 1, "YES" if good else "NO")

        

if __name__ == '__main__':
  main()
