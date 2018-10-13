#!/usr/bin/env python

import sys

_rest_tokens = []

def readToken():
  global _rest_tokens
  if not _rest_tokens:
    _rest_tokens = sys.stdin.readline().strip().split()
    _rest_tokens.reverse()
  return _rest_tokens.pop()

def log(*obj):
  str_obj = [str(o) for o in obj]
  sys.stderr.write(' '.join(str_obj) + '\n')

def main():
  case_count = int(readToken())
  for i in range(case_count):
    log('Process case #%d' % (i + 1))
    h = int(readToken())
    w = int(readToken())
    tiles = []
    is_impossible = False
    for j in range(h):
      tiles.append(list(readToken()))
    for y in range(h):
      for x in range(w):
        if tiles[y][x] == '.': continue
        if tiles[y][x] == '#':
          if y == h - 1 or x == w - 1:
            is_impossible = True
            break
          if tiles[y + 1][x] == '#' and tiles[y][x + 1] == '#' and tiles[y + 1][x + 1] == '#':
            tiles[y][x] = tiles[y + 1][x + 1] = '/'
            tiles[y][x + 1] = tiles[y + 1][x] = '\\'
          else:
            is_impossible = True
            break
      if is_impossible:
        break
    print 'Case #%d:\n%s' % (i + 1, 'Impossible' if is_impossible else '\n'.join([''.join(r) for r in tiles]))
      
if __name__ == '__main__':
  main()
