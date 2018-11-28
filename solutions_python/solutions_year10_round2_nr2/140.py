#! /usr/bin/python

import sys


def solve(n, k, b, t, pos, speed):
  num_chick_ok = 0
  t_cross = [t] * n
  t_cross_j = [-1] * n
  chick_ok = [False] * n

  for i in xrange(n):
    for j in xrange(i+1, n):
      if speed[i] > speed[j]:
        t_j = (pos[j] - pos[i]) / (speed[i] - speed[j])
        if t_j < t_cross[i]:
          t_cross[i] = t_j
          t_cross_j[i] = j

  nb_swap = 0
  first_chick_to_fail = n-1
  chicks_that_overtake = 0

  for i in xrange(n-1, -1, -1):
    if ((t_cross[i] == t and (pos[i] + t * speed[i]) >= b) or
        (t_cross_j[i] != -1 and chick_ok[t_cross_j[i]])):
      chick_ok[i] = True
      num_chick_ok += 1
      first_chick_to_fail = i-1

    else:
      if (pos[i] + t * speed[i]) >= b:   # can go to barn alone
        nb_swap += first_chick_to_fail - i - chicks_that_overtake
        chicks_that_overtake += 1
        num_chick_ok += 1

    if num_chick_ok >= k:
      return nb_swap

  return "IMPOSSIBLE"


fd = open(sys.argv[1])
num_cases = int(fd.readline())

for i in range(0, num_cases):
  (n, k, b, t) = [int(item) for item in fd.readline().split(" ")]
  pos = [int(item) for item in fd.readline().split(" ")]
  speed = [int(item) for item in fd.readline().split(" ")]
  output = solve(n, k, b, t, pos, speed)
  print "Case #%d:" % (i+1), output

