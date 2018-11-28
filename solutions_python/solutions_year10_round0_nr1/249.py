#!/usr/bin/python

import sys

def IsOn(N, K):
  return (((K+1) % (2**N)) == 0)

def main(argc, argv):
  ifile = open(argv[1], 'r')

  case = 0
  ifile.readline()
  for line in ifile:
    N, K = line.split()
    case += 1
    if IsOn(int(N), int(K)):
      print 'Case #' + str(case) + ': ON'
    else:
      print 'Case #' + str(case) + ': OFF'


if __name__ == "__main__":
  main(len(sys.argv), sys.argv)
