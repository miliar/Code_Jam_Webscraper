#!/usr/bin/python
import sys

def fix(N):
  for i in range(len(N)-1):
    if N[i] > N[i+1]:
      break
  else:
    return N

  for j in xrange(i-1, -1, -1):
    if N[j] != N[i]:
      break
  else:
    j = -1

  j += 1
  N[j] -= 1

  for k in range(j+1, len(N)):
    N[k] = 9

  return N

def calc(N):
  N = fix(N)
  return int("".join(str(d) for d in N))  

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(1,n+1):
    N = [int(di) for di in d[j][:-1]]
    print "Case #%d: %s" % (j, calc(N))

main()
