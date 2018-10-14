#!/usr/bin/env python
# Google Code Jam 2008 Qualifcations, Task B
# Solution by Sebastian Hagen
# language: Python 2.5
# This program reads input from stdin and writes output to stdout.

def strptime(s):
   (h,m) = s.split(':')
   return int(h,10)*60+int(m,10)

class TrainAllocator:
   IN = 1  # train becoming ready for being sent out
   OUT = 2 # scheduled train departure
   def __init__(self, turnaround_time):
      self.A_events = []
      self.B_events = []
      self.turnaround_time = turnaround_time
   
   def add_trip(self, src, src_ts, dst_ts):
      if (src == 'A'):
         se = self.A_events
         de = self.B_events
      elif (src == 'B'):
         se = self.B_events
         de = self.A_events
      else:
         raise ValueError('Invalid src value %r.' % (src,))
      
      se.append((src_ts, self.OUT))
      de.append((dst_ts + self.turnaround_time, self.IN))
   
   def tc_compute(self, sta):
      if (sta == 'A'):
         events = self.A_events
      elif (sta == 'B'):
         events = self.B_events
      else:
         raise ValueError('Invalid sta value %r.' % (sta,))
      
      events.sort()
      rv = 0 # trains we need to have locally at 00:00
      tc = 0 # locally remaining trains
      for event in events:
         (ts, io) = event
         if (io == self.IN):
            # Add train to local reserve
            tc += 1
            continue
         if (tc > 0):
            # Send out train from reserve
            tc -= 1
            continue
         # Add new train to initial allocation
         rv += 1
      
      return rv
   
   @classmethod
   def build_from_file(cls, f):
      tt = int(f.readline().strip())
      return cls(tt)
   
   @classmethod
   def solve_from_file(cls, f):
      ta = cls.build_from_file(f)
      (nac, nbc) = f.readline().strip().split()
      nac = int(nac)
      nbc = int(nbc)
      for i in range(nac):
         ta.add_trip('A', *[strptime(x) for x in f.readline().strip().split()])
      for i in range(nbc):
         ta.add_trip('B', *[strptime(x) for x in f.readline().strip().split()])
      return (ta.tc_compute('A'), ta.tc_compute('B'))


if (__name__ == '__main__'):
   import sys
   tc_count = int(sys.stdin.readline().strip())
   for i in range(tc_count):
      sys.stdout.write('Case #%d: %d %d\n' % ((i+1,) + TrainAllocator.solve_from_file(sys.stdin)))
