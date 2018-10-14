"""
Clive Gifford's Solution to the "Train Timetable" problem, GCJ 2008
"""

import sys

def HHMM2Mins(HHMM):
   HH, MM = map(int, HHMM.split(':'))
   return HH * 60 + MM
   
def OptimiseTrips(trips):
   START, STOP, SRC, DST = range(4)
   link = 0
   for n1 in xrange(len(trips)):
      for n2 in xrange(n1+1, len(trips)):
         if trips[n1][STOP] <= trips[n2][START] and \
            trips[n1][DST] in "AB" and \
            trips[n1][DST] == trips[n2][SRC]:
            trips[n1][DST] = trips[n2][SRC] = "T" + str(link)
            link += 1
            break 

fin = file(sys.argv[1])
fout = file(sys.argv[2], "wt")

numCases = int(fin.readline())
for case in xrange(numCases):
   turnaroundtime = int(fin.readline())
   nA, nB = map(int,fin.readline().split())
   trips = []
   for trip in xrange(nA):
      start, stop = map(HHMM2Mins, fin.readline().split()) 
      trips.append([start, stop + turnaroundtime, "A", "B"])
   for trip in xrange(nB):
      start, stop = map(HHMM2Mins, fin.readline().split()) 
      trips.append([start, stop + turnaroundtime, "B", "A"])
#   print trips   
   trips.sort()
#   print trips
   OptimiseTrips(trips)
#   print trips
   tA = len([True for (start, stop, src, dest) in trips if src == "A"])
   tB = len([True for (start, stop, src, dest) in trips if src == "B"])
   fout.write("Case #%d: %d %d\n" % (case+1, tA, tB))   
   