#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint

def countLetters(word):
  letters = [word[0]]
  count = [1]
  for c in word[1:]:
    if c == letters[-1]:
      count[-1] += 1
    else:
      letters.append(c)
      count.append(1)

  return letters, count

def solveCase(words):
  letters, c1 = countLetters(words[0])

  counts = [c1]
  for word in words[1:]:
    l, c = countLetters(word)
    if l != letters:
      return 'Fegla Won'

    counts.append(c)

  r = 0

  for i in range(len(letters)):
    numc = [c[i] for c in counts]
    maxn = max(numc)
    minn = min(numc)
    
    r1 = 100000
    for j in range(minn, maxn + 1):
      r2 = 0
      for n in numc:
        r2 += abs(j - n)
      if r2 < r1:
        r1 = r2
    r += r1

  return r

def solve(s):
  t = int(s.readline())

  for i in range(t):
    n = int(s.readline())
    words = [s.readline().strip() for i in range(n)]
    print('Case ' + str(i + 1))
    r = solveCase(words)
    print(r)
    yield str(r)

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': ' + case + '\n')
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)
