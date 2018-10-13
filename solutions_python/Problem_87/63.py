from __future__ import division
import collections

f = open('A-large.in', 'r')
cases = int(f.next())
for c in xrange(cases):
  X, S, R, t, N = [int(x) for x in f.next().split()]
  walkway_speeds = collections.defaultdict(int)
  used = 0
  for n in xrange(N):
    B, E, w = [int(x) for x in f.next().split()]
    walkway_speeds[w] += (E - B)
    used += (E - B)
  walkway_speeds[0] = X - used
  
  remaining_t = t
  time_used = 0
  for speed, distance in sorted(walkway_speeds.iteritems()):
    # Greedily consume time
    if remaining_t > 0:
      time_spendable = distance / (speed + R)
      if time_spendable <= remaining_t:
        time_used += time_spendable
        remaining_t -= time_spendable
      else:
        time_used += remaining_t + (distance - (remaining_t * (speed + R))) / (speed + S)
        remaining_t = 0
    else:
      time_used += distance / (speed + S)
  
  print 'Case #%d: %.9f' % (c + 1, time_used)