#!/usr/bin/python

import sys

def parse(f):
  H, W = map(int, f.readline().strip().split(' '))
  mx = []
  mx.append([100000 for i in range(W+2)])
  for h in range(H):
    mx.append([100000] + map(int, f.readline().strip().split(' ')) + [100000])
  mx.append([100000 for i in range(W+2)])

  return (H, W, mx)

def solve(o):
  H, W, mx = o
  basins = []
  links = [[[] for i in range(W)] for i in range(H)]
  for h in range(1, H+1):
    for w in range(1, W+1):
      alt = [(mx[h-1][w],1,h-1,w), (mx[h][w-1],2,h,w-1), (mx[h][w+1],3,h,w+1), (mx[h+1][w],4,h+1,w)]
      m = min(alt)
      if mx[h][w] <=  m[0]:
        basins.append((h-1,w-1))
      else:
        links[m[2]-1][m[3]-1].append((h-1,w-1))
        links[h-1][w-1].append((m[2]-1,m[3]-1))

  chars = [[None for i in range(W)] for i in range(H)] 
  ch = 97 # a
  for h in range(0, H):
    for w in range(0, W):
      if (None == chars[h][w]):
        fill(chars, links, h, w, chr(ch))
        ch += 1

  # print basins
  # print links
  # print chars
  print '\n'.join(map(lambda row: ' '.join(row), chars))

def fill(chars, links, h, w, ch):
  chars[h][w] = ch
  q = list(links[h][w])
  while 0 < len(q):
    lh, lw = q.pop()
    if None == chars[lh][lw]:
      chars[lh][lw] = ch
      q += list(links[lh][lw])

def main():
  f = sys.stdin
  n = int(f.readline())
  for i in range(n):
    o = parse(f)
    # print o
    print 'Case #%d:' % (i+1)
    solve(o)

if __name__ == '__main__':
  main()
