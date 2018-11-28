#!/usr/bin/python

MAX_ALT = 11000

def is_valid_index(i, j, alts):
  return i >= 0 and j >= 0 and i < len(alts) and j < len(alts[i])

def find_flow_dir(i, j, alts):
  dirs = [(alts[i][j], (i, j)),
          (alts[i - 1][j] if is_valid_index(i - 1, j, alts) else MAX_ALT, (i - 1, j)),
          (alts[i][j - 1] if is_valid_index(i, j - 1, alts) else MAX_ALT, (i, j - 1)),
          (alts[i][j + 1] if is_valid_index(i, j + 1, alts) else MAX_ALT, (i, j + 1)),
          (alts[i + 1][j] if is_valid_index(i + 1, j, alts) else MAX_ALT, (i + 1, j))]
  return min(dirs, key=lambda x: x[0])[1]

def flow(i, j, n, ans, alts, eq):
  while ans[i][j] == -1:
    ans[i][j] = n
    ni, nj = find_flow_dir(i, j, alts)
    if (ni, nj) == (i, j): # found a sink
      break
    i, j = ni, nj
  eq[n] = ans[i][j]

def print_basin(basin, f):
  for row in basin:
    f.write(' '.join(map(str, row)) + '\n')


def parent(num, eq):
  if eq[num] != num:
    eq[num] = parent(eq[num], eq)
  return eq[num]

def to_alph(basin, eq):
  nums_seen = {}
  count = 0
  for i in xrange(H):
    for j in xrange(W):
      p = parent(basin[i][j], eq)
      if p not in nums_seen:
        nums_seen[p] = count
        count += 1
      basin[i][j] = chr(ord('a') + nums_seen[p])
    

f = open('B-large.in', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

N = int(lines[0])

f = open('B-large.out', 'w')
line_num = 1
for case in xrange(1, N + 1):
  H, W = map(int, lines[line_num].split(' '))
  alts = [0]*H
  for i in xrange(H):
    alts[i] = map(int, lines[line_num + i + 1].split(' '))
    assert len(alts[i]) == W

  ans = [0] * H
  for i in xrange(H):
    ans[i] = [-1] * W
  
  equivalencies = {}
  count = 0
  for i in xrange(H):
    for j in xrange(W):
      if ans[i][j] == -1:
        flow(i, j, count, ans, alts, equivalencies)
        count += 1

  to_alph(ans, equivalencies)
  f.write('Case #%d:\n' % case)
  print_basin(ans, f)
  line_num += 1 + H

f.close()
