#!/usr/bin/env python
# Marco Gallotta
import math, sys, itertools

T = int(raw_input())
for case in xrange(1, T+1):
  N = raw_input()
  ans = 100000000000000000000000000
  for i in xrange(len(N)):
    for j in xrange(len(N)):
      num = list(N)
      num[i], num[j] = num[j], num[i]
      num = num[:i+1] + map(str, sorted(map(int, list(num[i+1:]))))
      num = int("".join(num))
      if num > int(N) and num < ans:
        ans = num
  num = map(str, sorted(map(int, list(N))))
  zeroes = num.count("0")
  num[0], num[zeroes] = num[zeroes], num[0]
  num = int(num[0] + "0" + "".join(num[1:]))
  if num > int(N) and num < ans:
    ans = num
  num *= 10**(N.count("0")+1)
  if num > int(N) and num < ans:
    ans = num
  print "Case #%d: %d" % (case, ans)
