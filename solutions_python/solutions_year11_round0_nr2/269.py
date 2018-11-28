#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2011 May  7
import sys
import math
import functools

def add(a, b):
  return a.__xor__(b)

def pp(listelt):
  if len(listelt) == 0:
    return "[]"
  res = "["
  for x in listelt:
    res = res + x + ", "
  res = res[:-2]
  return res + "]"

def is_valid(values):
  x_total = functools.reduce(lambda x, y : add(x,y), values)
  if ((x_total % 2)):
    return True
  return False

def main():
  file = open(sys.argv[1])

  nb_cases = int(file.readline())

  for case_nb in range(1, nb_cases + 1):
    combine_dict = {}
    opposed_dict = {}
    line = file.readline().replace('\n','')
    tokens = line.split(' ')
    i = 0
    C = int(tokens[0])
    c_elts = tokens[i+1:i+1+C]
    for x in c_elts:
      combine_dict[x[:2]] = x[2]
      combine_dict[x[:2][::-1]] = x[2]
    i = i + 1 + C
    D = int(tokens[i])
    d_elts = tokens[i+1:i+1+D]
    for x in d_elts:
      opposed_dict[x] = True
      opposed_dict[x[::-1]] = True
    i = i + 1 + D
    N = int(tokens[i])
    n_elts = tokens[i+1]
    elts = []
    for x in n_elts:
      if (len(elts) > 0):
        tst = elts[len(elts) - 1] + x
        if tst in combine_dict:
          elts[len(elts) - 1] = combine_dict[tst]
        else:
          elts.append(x)
          for a in elts[0:len(elts) - 1]:
            key = a + x
            if key in opposed_dict:
              elts = []
      else:
        elts.append(x)

    print("Case #%s: " % case_nb + "%s" % pp(elts))





  file.close()

if __name__ == "__main__":
  main()
