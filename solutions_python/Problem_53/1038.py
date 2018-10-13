#! /usr/bin/env python

import numpy as np
import sys

class Snappers(object):
  """Snappers question in qualification round of GCJ 2010"""
  def __init__(self, inpfile):
    self.infile = inpfile
    self.numtests = 0
    self.NK = [(0,0)]
  
  def read_data(self):
    # import pdb; pdb.set_trace()
    f = open(self.infile, 'r')
    self.numtests = int(f.readline())
    for line in f:
      nums = line.split()
      self.NK.append( (int(nums[0]), int(nums[1])) )
    f.close()
  
  def start_snapping(self, N, K):
    snapper_states = np.array(np.zeros(N), dtype=bool)
    bulb_on = False
    snaps = 1
    while(snaps <= K):
      is_active = 0
      while is_active < N and snapper_states[is_active]:
        snapper_states[is_active] = False
        is_active += 1
      if is_active < N:
        snapper_states[is_active] = True
      if snapper_states.all():
        bulb_on = True
      else:
        bulb_on = False
      snaps += 1
    return bulb_on
  
  def start_sim(self):
    self.read_data()
    i=1
    while(i<=self.numtests):
      # self.NK[i][0] is N and self.NK[i][1] is K
      if self.start_snapping(self.NK[i][0], self.NK[i][1]):
        print "Case #{0}: ON".format(i)
      else:
        print "Case #{0}: OFF".format(i)
      i += 1
  


def main():
  """start the snapping simulations"""
  print "Input file name: "
  inpfile = sys.stdin.readline()
  s = Snappers(inpfile.strip())
  s.start_sim()


if __name__ == "__main__":
  main()
