#!/usr/bin/env python

from sys import stdin

def f():
   wanted_row = int(stdin.readline().strip())
   ret = set()
   for r in xrange(1, 5):
      line = stdin.readline()
      if r == wanted_row:
         ret = set(map(int, line.split()))
   return ret

def main():
   TC = int(stdin.readline().strip())
   for tc in xrange(1, TC+1):
      set1 = f()
      set2 = f()
      cset = set1 & set2
      if len(cset) == 0:
         print 'Case #%d: Volunteer cheated!' % tc
      elif len(cset) > 1:
         print 'Case #%d: Bad magician!' % tc
      else:
         print 'Case #%d: %d' % (tc, cset.pop())
   return 0

if __name__ == '__main__': main()
