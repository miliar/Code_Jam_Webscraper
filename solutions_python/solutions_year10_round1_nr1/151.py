import sys
import itertools

global cache

print 'magic'
f = "mytest"
f = "A-small-attempt0"
f = "A-large"
infile = open(f+".in", "r")
outfile = open(f+".out", "w")

def ReadInts(foo):
  return list(map(foo, infile.readline().strip().split(" ")))

def found(l, s):
  for i in l:
    if s in i: return True
  return False

T = ReadInts(int)[0]
for each in range (1, T+1):
  cache = {}
  (N,K) = ReadInts(int)

  for i in range(N):
    l = ReadInts(str)
    for j in range(N):
       cache[(N-j-1,N-i-1)] = l[0][j]
       
  for j in range(N):
    i = 0
    while i < N:
      if cache[(i,j)] == '.': break
      i += 1
    empty = i
    for p in range(i+1,N):
      if cache[(p,j)] != '.':
        cache[(empty,j)] = cache[(p,j)]
        cache[(p,j)] = '.'
        empty += 1

  lists = []
  for i in range(N):
    x = ''
    y = ''
    for j in range(N):
      x += cache[(i,j)]
      y += cache[(j,i)]
    lists.append(x)
    lists.append(y)

  for i in range(K-1, N):
    x = ''
    y = ''
    z = ''
    w = ''
    for j in range(i+1):
      x += cache[(j,i-j)]
      y += cache[(N-1-j,N-1-i+j)]
      z += cache[(j,N-1-i+j)]
      w += cache[(N-1-j,i-j)]
    lists.append(x)
    lists.append(y)
    lists.append(z)
    lists.append(w)

  output = "Neither"
  if found(lists, 'R' * K):
    output = "Red"
  if found(lists, 'B' * K):
    if output == 'Red':
      output = 'Both'
    else: output = 'Blue'
  
  print 'Case #%d: %s\n' % (each, output)
  outfile.write('Case #%d: %s\n' % (each, output))
