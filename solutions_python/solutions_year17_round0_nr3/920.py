#!/usr/bin/env python

from collections import defaultdict

with open('C-large.in') as f:
  T = int(f.readline())
  with open('C-large.out', 'w') as of:
    for t in range(0,T):
      l = f.readline().strip().split()
      N = int(l[0])
      K = int(l[1])
      k = K
      n = N
      level_size = 1
      mp = defaultdict(int)
      mp[(N, 0)] = 1
      while k > 0:
        newmp = defaultdict(int)
        for (choice, cnt) in mp.items():
          for n in choice:
            if n > 0:
              if n % 2 == 1:
                newmp[(n//2, n//2)] += cnt
              else:
                newmp[(n//2, n//2-1)] += cnt
        mp = newmp
        if k > level_size:
          k -= level_size
          level_size *= 2
        else:
          break
      if len(mp.keys()) > 2:
        raise(ValueError('too many keys'))
      sorted_choices = sorted(mp.keys())
      if mp[sorted_choices[-1]] >= k:
        res = str(sorted_choices[-1][0]) + ' ' + str(sorted_choices[-1][1])
      else:
        res = str(sorted_choices[0][0]) + ' ' + str(sorted_choices[0][1])
      of.write('Case #' + str(t+1) + ': ' + res + '\n')
