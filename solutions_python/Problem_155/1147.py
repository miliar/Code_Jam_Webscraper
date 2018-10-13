from itertools import *
from pprint import pprint

def solve(fi, fo, ti):
  l = fi.readline().strip().split(' ')
  sm = int(l[0])
  sis = [int(s) for s in l[1]]

  o = 0
  stood = 0
  for i in range(len(sis)):
    si = sis[i]
    if si != 0:
      if stood  < i:
        new = (i - stood)
        o += new
        stood += new

      stood += si


  return o

def main(f):
  fi = open(f + '.in')
  fo = open(f + '.out', 'w')

  T = int(fi.readline())
  for ti in range(T):
    #fi.readline().strip()
    out = solve(fi, fo, ti)
    fo.write("Case #%d: %s\n" % ((ti+1), out) )
    print "Case #%d: %s" %  ((ti+1), out) 

if __name__ == "__main__":
  main('A-large')