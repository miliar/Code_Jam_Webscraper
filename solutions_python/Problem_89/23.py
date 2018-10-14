#!/usr/bin/python -u

import sys,re,math

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

debugprint = 10

def primes(n): 
  if n==2: return [2]
  elif n<2: return []
  s=range(3,n+1,2)
  mroot = n ** 0.5
  half=(n+1)/2-1
  i=0
  m=3
  while m <= mroot:
    if s[i]:
      j=(m*m-3)/2
      s[j]=0
      while j<half:
        s[j]=0
        j+=m
    i=i+1
    m=2*i+3
  return [2]+[x for x in s if x]

def maxpowers(n):
  ls = []
  ps = primes(n)
  for p in ps:
    l = int(math.log(n, p))
    ls.append(l)
  return ls

def debug(str, lvl=5):
  if debugprint > lvl: print "[DEBUG]", str

def handleonecase(line1):
  #TODO
  n = int(line1[0])
  m = maxpowers(n)
  if n <= 1: return 0
  mincalls = len(m)
  maxcalls = 1+sum(m)
  return maxcalls-mincalls

maxcases = 0
casenum = 0

line = infile.readline().strip()
maxcases = int(line)
while line:
  casenum = casenum + 1
  if casenum > maxcases: break
  line1 = infile.readline().strip().split()
#  line2 = infile.readline().strip().split()
  result = handleonecase(line1)
  print "Case #" + str(casenum) + ": " + str(result)




