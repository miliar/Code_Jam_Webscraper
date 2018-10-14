#!/usr/bin/python
import sys

def calc(board):
  res_b = []
  for i in xrange(len(board)):
    res_b.append([])
    for j in xrange(len(board[0])):
      res_b[-1].append(board[i][j])

  for i in xrange(len(board)):
    for j in xrange(len(board[0])):
      if res_b[i][j] == "#":
        if (i == (len(board)-1) or j == (len(board[0])-1) or
           board[i+1][j] != "#" or board[i][j+1] != "#" or
           board[i+1][j+1] != "#"):
          return "Impossible"
        res_b[i][j] = "/"
        res_b[i+1][j] = "\\"
        res_b[i][j+1] = "\\"
        res_b[i+1][j+1] = "/"
  return "\n".join(["".join(line) for line in res_b])

def main(filename):
  f = file(filename)
  n = int(f.readline())
  for case in xrange(1, n+1):
    R,C = map(int, f.readline().split())
    board = []
    for i in xrange(R):
      board.append(list(f.readline().rstrip('\n')))
    print "Case #%d:\n%s" % (case, calc(board))

if __name__ == "__main__":
  main(sys.argv[1])
