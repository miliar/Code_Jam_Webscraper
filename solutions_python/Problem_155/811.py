#!/usr/bin/env python
import sys

if __name__ == '__main__':
   if len(sys.argv) != 2:
      print("usage: %s [input file]"%(sys.argv[0]))
      sys.exit(1)
   with open(sys.argv[1]) as f:
      num_cases = f.readline()
      for n, line in enumerate(f):
         max_, shy = line.split(' ', 1)
         shys = [int(x) for x in shy.strip()]
         c_up = 0
         c_need = 0
         for i, shy in enumerate(shys):
            if c_up < i:
               c_need += 1
               c_up += 1
            c_up += shy
         print("Case #%d: %d"%(n+1, c_need))
