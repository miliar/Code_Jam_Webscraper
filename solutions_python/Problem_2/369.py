#!/usr/bin/python

import sys

try:
  import psyco
  psyco.full()
except Exception, e:
  pass

class Station:

  def __init__(self, the_trips, turnaround, id):
    self.turnaround = turnaround
    self.id = id

    self.MISSING = 0
    self.parked = {}

    self.trips = {}
    def add_trip(str):
      h_m = map(lambda x: map(int, x.split(':')), str.split(' '))
      departing = h_m[0][0] * 60 + h_m[0][1]
      if not self.trips.has_key(departing):
        self.trips[departing] = []
      self.trips[departing].append(h_m[1][0] * 60 + h_m[1][1])
    for t in the_trips:
      add_trip(t)

    #print >> sys.stderr, self.trips

    self.transit = {}

  def leave(self, t):
    if self.trips.has_key(t): # trip leaving
      for arriving in self.trips[t]:
        if not self.transit.has_key(arriving):
          self.transit[arriving] = 1
        else:
          self.transit[arriving] += 1


        found = False
        if len(self.parked):
          first = min(self.parked.keys()) # O(N), use something better.
          if first <= t:
            self.parked[first] -= 1
            found = True
            if self.parked[first] == 0:
              del self.parked[first]
        if not found:
          self.MISSING += 1

        #print >> sys.stderr, 't:', t, self.id, 'traing leaves', 'MISSING', self.MISSING
  
  def count_arrivals(self, N, t):
    if N:
      t += self.turnaround
      if self.parked.has_key(t):
        self.parked[t] += N
      else:
        self.parked[t] = N

  def trains_ready_to_arrive(self, t):
    ret = 0
    if self.transit.has_key(t):
      ret = self.transit[t]
      del self.transit[t]
    #if ret:
    #  print >> sys.stderr, 't:', t, self.id, ret, 'trains arrive(s)'
    return ret

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  NTEST =  int(f.readline())

  for i in xrange(NTEST):
    #TODO: put this
    print ('Case #%d:' % (i + 1)),

    TURNAROUND = int(f.readline())
    #print >> sys.stderr, 'TURNAROUND', TURNAROUND
    NAB, NBA = map(int, f.readline().split())
    #print>> sys.stderr, 'NAB NBA', (NAB, NBA)

    AB = []
    for i in xrange(NAB):
      AB.append(f.readline().strip())
    BA = []
    for i in xrange(NBA):
      BA.append(f.readline().strip())
    #print AB, BA

    st_a = Station(AB, TURNAROUND, 'A->B')
    st_b = Station(BA, TURNAROUND, 'B->A')

    for t in xrange(0, 24 * 60 + 1): # exagerating :-) 24 * 60 is Ok
      st_a.count_arrivals(st_b.trains_ready_to_arrive(t), t)
      st_b.count_arrivals(st_a.trains_ready_to_arrive(t), t)
      st_a.leave(t)
      st_b.leave(t)

    print st_a.MISSING, st_b.MISSING
