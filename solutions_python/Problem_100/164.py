#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2012

@author: daniel
'''
from contextlib import closing as c

class CountPlays(object):
  def __init__(self, inloc, outloc):
    with c(open(inloc)) as self.fhi, c(open(outloc, 'w')) as self.fho:
      cases = int(self.fhi.readline())

      for case in range(1, cases + 1):
        self.Count(case)

  def Count(self, case):
    levels = int(self.fhi.readline())

    plays = 0
    stars = 0

    onestars = {}
    twostars = {}

    for level in range(1, levels + 1):
      one, two = map(int, self.fhi.readline().split())
      onestars[level] = [one, False, level]
      twostars[level] = [two, False, level]

    while not all([level[1] for level in twostars.values()]):
      canbeattwos = [l for l in twostars.values() if l[0] <= stars and not l[1]]
      for _stars, _beaten, level in canbeattwos:
        plays += 1
        twostars[level][1] = True
        stars += 1 if onestars[level][1] else 2
        onestars[level][1] = True

      canbeatones = [l for l in onestars.values() if l[0] <= stars and not l[1]]
      canbeatones.sort(key = lambda (_s, _b, l): twostars[l][0])

      if not canbeatones and not canbeattwos:
        return self.fho.write("Case #%d: Too Bad\n" % case)

      if not canbeattwos:
        _stars, _beaten, level = canbeatones.pop()
        onestars[level][1] = True
        plays += 1
        stars += 1

    self.fho.write("Case #%d: %d\n" % (case, plays))



if __name__ == '__main__':
    CountPlays(r'../data/round1b_large.txt', '../data/round1b_large-out.txt')
