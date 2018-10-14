#!/usr/bin/python -u

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

debugprint = 0

def debug(str, lvl=5):
  if debugprint > lvl: print "[DEBUG]", str

class segment:
  def __init__(self, length, basespeed):
    self.length = length
    self.basespeed = basespeed
  def dump(self):
    debug([self.length, self.basespeed])
  def computetimenorun(self):
    if self.basespeed == 0: return 0
    return 1.*self.length/self.basespeed
  def computetime(self, secondstorun, rundiff):
    # rundiff is run minus walk speed
    if rundiff <= 0: return self.computetimenorun()
    if secondstorun <= 0: return self.computetimenorun()
    # TODO
    self.dump()
    debug(["secondstorun,rundiff", secondstorun, rundiff])

    if 1.*self.length/(self.basespeed + rundiff) <= secondstorun:
      # we can run the whole segment
      debug("ran full length")
      return 1.*self.length/(self.basespeed + rundiff)
    # else run for a bit, walk for a bit
    debug("ran part length")
    t1 = secondstorun
    r1 = (self.basespeed + rundiff)
    d1 = r1*t1
    d2 = self.length - d1
    r2 = self.basespeed
    t2 = 1.*d2/r2
    return t1+t2
  def getlength(self): return self.length
  def getbasespeed(self): return self.basespeed

def sortbyspeed(segments):
  for i in range(0, len(segments)-1):
    for j in range(i, len(segments)):
      if segments[i].getbasespeed() > segments[j].getbasespeed():
        t = segments[i]
        segments[i] = segments[j]
        segments[j] = t
  return segments

def handleonecase(line1):
  #TODO
  X = int(line1[0])
  S = int(line1[1])
  R = int(line1[2])
  t = int(line1[3])
  N = int(line1[4])
  totalwalkwaylength = 0
  segments = []
  for i in range(0,N):
    walkwaydata = infile.readline().strip().split()
    Bi = int(walkwaydata[0])
    Ei = int(walkwaydata[1])
    wi = int(walkwaydata[2])
    s = segment(Ei-Bi, wi+S)
    segments.append(s)
    totalwalkwaylength = totalwalkwaylength + Ei - Bi
  s = segment(X - totalwalkwaylength, S)
  segments.append(s)

  # sort slowest to fastest
  segments = sortbyspeed(segments)

  debug([X, S, R, t, N])
  for s in segments: s.dump()

  # TODO remove this
  #t = 0

  totaltime = 0
  segmenttime = 0
  for s in segments:
    segmenttime = s.computetime(t, R-S)
    totaltime = totaltime + segmenttime
    if segmenttime > t:
      t = 0
    else:
      t = t - segmenttime
    debug(segmenttime)
  return totaltime

maxcases = 0
casenum = 0

line = infile.readline().strip()
maxcases = int(line)
while line:
  casenum = casenum + 1
  if casenum > maxcases: break
  line1 = infile.readline().strip().split()
#  line2 = infile.readline().strip().split()
  result = handleonecase(line1)
  print "Case #" + str(casenum) + ": " + str(result)




