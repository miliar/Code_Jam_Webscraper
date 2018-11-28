#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2011 May  7
import sys
import math
import functools


def main():
  file = open(sys.argv[1])

  nb_cases = int(file.readline())

  for case_nb in range(1, nb_cases + 1):
    lineA = file.readline().replace('\n','')
    lineB = file.readline().replace('\n','')
    N = int(lineA)
    tokens = map(lambda x : int(x), lineB.split(' '))
    wrong = 0
    i = 1
    for n in tokens:
      if n != i:
        wrong = wrong + 1
      i = i + 1

    print("Case #%s: " % case_nb + "%s.000000" % (wrong))





  file.close()

if __name__ == "__main__":
  main()
