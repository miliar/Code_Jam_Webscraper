#!/usr/bin/env python2
import sys

def work_it(string):
  lst = [int(x) for x in string]
  pool = 0
  need = 0
  for x in lst:
    pool += (x - 1)
    if pool == -1:
      need += 1
      pool += 1
  return need


def main():
  with open("in", 'rU') as f:
    lines = f.readline()
  
    for i in xrange(int(lines)):
      sm, string = f.readline().split()
      out = work_it(string)
      # line = f.readline()
      print "Case #{}: {}".format(i + 1, out)


if __name__ == '__main__':
  main()
