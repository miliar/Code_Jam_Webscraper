#! /usr/bin/env python2

from __future__ import division

def ETA(stockpile, cps, x):
  (x - stockpile) / cps

def worthit(c, f, x, cps):
  # worth it if the time until we can buy a factory
  #    (c / cps)
  # plus the new time until completion
  #    (x / (cps + f))
  # is smaller than the time spent simply waiting
  #    (x / cps)
  return ((c / cps) + x / (cps + f)) < (x / cps)

def main():
  # most efficient way of doing this is by buying factories as fast as possible
  test_num = int(raw_input())
  for test in range(test_num):
    c, f, x = [float(elem) for elem in raw_input().split()]
    totaltime = 0.0
    cps = 2.0
    done = False

    while not done:
      # progressively lower target, buying factories
      if worthit(c, f, x, cps):
        totaltime += c / cps
        cps += f
      else:
        # last invocation
        totaltime += x / cps
        done = True

    print 'Case #%i: %.7f' % (test + 1, totaltime)


if __name__ == '__main__':
  main()
