#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2011 May  7
import sys
import math
import functools

def add(a, b):
  return a.__xor__(b)

def eq(a, b):
  b_a = bin(a)[2:]
  b_b = bin(b)[2:]
  l = min (len(b_a), len(b_b))
  r_a = b_a[::-1][:l]
  r_b = b_b[::-1][:l]
  if (r_a == r_b):
    return True
  return False

def main():
  file = open(sys.argv[1])

  nb_cases = int(file.readline())

  for case_nb in range(1, nb_cases + 1):
    strA = file.readline().replace('\n','')
    strB = file.readline().replace('\n','')
    candy = int(strA)
    values = sorted(map(lambda x : int(x), strB.split(' ')))
    flag = False
    for i in range(1, candy):
      sean = values[i:]
      patr = values[:i]
      s = functools.reduce(lambda x, y: add(x,y), sean)
      p = functools.reduce(lambda x, y: add(x,y), patr)
      if (eq(s,p)):
        print("Case #%s: " % case_nb + "%s" % sum(sean))
        flag = True
        break
    if not flag:
      print("Case #%s: " % case_nb + "%s" % 'NO')




  file.close()

if __name__ == "__main__":
  main()
