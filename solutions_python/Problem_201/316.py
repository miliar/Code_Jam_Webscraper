#!/usr/bin/env python

def solve(case_nr):
  [N, K] = map(int, raw_input().split())
  maxLR = 0
  minLR = 0
  
  if (K != N):
    intervals = {}
    intervals[N] = 1
    
    while K>0:
      interval_size = max(intervals.iterkeys())
      nr_intervals = intervals.pop(interval_size)
      
      nr_place = min(K, nr_intervals)
      
      if (nr_place < nr_intervals):
        intervals[interval_size] = nr_intervals - nr_place
        
      if (interval_size % 2 == 1):
        new_interval = (interval_size - 1) / 2
        existing_nr = intervals.get(new_interval, 0)
        intervals[new_interval] = existing_nr + 2*nr_place
        maxLR = new_interval
        minLR = new_interval
      else:
        new_interval = interval_size / 2
        existing_nr = intervals.get(new_interval, 0)
        intervals[new_interval] = existing_nr + nr_place
        maxLR = new_interval
        new_interval = (interval_size-2) / 2
        existing_nr = intervals.get(new_interval, 0)
        intervals[new_interval] = existing_nr + nr_place
        minLR = new_interval
        
      K -= nr_place
    #print intervals

  print "Case #%d: %d %d" % (case_nr, maxLR, minLR)


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
