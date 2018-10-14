import sys
import itertools

global l

f = "mytest"
f = "A-large"
infile = open(f+".in", "r")
outfile = open(f+".out", "w")

def ReadInts(foo):
  return list(map(foo, infile.readline().strip().split(" ")))

def adds(s):
    l.add(s)
    for j in range(len(s)):
      if s[j] == '/' and j>0:
        l.add(s[:j])
    return

def ispresent(f):
  c = 0
  if f not in l:
    for j in range(len(f)):
      fd = ''
      if f[j]=='/' : fd = f[:j]
      if j == len(f)-1: fd = f
      if fd != '' and fd not in l:
          c += 1
          adds(fd)
  return c
    
T = ReadInts(int)[0]
for each in range (1, T+1):
  (N,M) = ReadInts(int)
  l = set()
  for i in range(N):
    adds(ReadInts(str)[0])

  output = 0
  for i in range(M):
    f = ReadInts(str)[0]
    output += ispresent(f)

  print 'Case #%d: %s\n' % (each, output)
  outfile.write('Case #%d: %s\n' % (each, output))
