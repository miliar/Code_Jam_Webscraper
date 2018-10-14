#!/usr/bin/python

import sys

def do_label(M, L, r, c, tag):
  delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
  path = []
  while True:
    path.append((r,c))
    L[r][c] = tag
    themin = M[r][c]
    next = None
    for d in delta:
      nr, nc = r + d[0], c + d[1]
      if nr >= 0 and nr < len(M) and nc >= 0 and nc < len(M[0]):
        if M[nr][nc] < themin:
          themin = M[nr][nc]
          next = (nr, nc)
    if next == None:
      return
    elif L[next[0]][next[1]] != None:
      for p in path:
        L[p[0]][p[1]] = L[next[0]][next[1]]
      return
    else:
      (r,c) = next

def solve(M):
  label = []
  for i in xrange(len(M)):
    label.append(len(M[0]) * [None])
  tag = 1
  for r in xrange(len(M)):
    for c in xrange(len(M[0])):
      if label[r][c] == None:
        do_label(M, label, r, c, tag)
        tag += 1
  tag = 'a'
  known = {}
  for r in xrange(len(M)):
    for c in xrange(len(M[0])):
      if not known.has_key(label[r][c]):
        known[label[r][c]] = tag
        tag = chr(ord(tag) + 1)
      print known[label[r][c]],
    print
    
if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())
  for i in xrange(NTEST):
    print ('Case #%d:' % (i + 1))
    ROWS,__ = map(int, f.readline().strip().split())
    M = []
    for i in xrange(ROWS):
      M.append(map(int, f.readline().strip().split()))
    solve(M)
