from __future__ import with_statement
from math import pow
import sys

def parseIntLine(line):
  return [int(x) for x in line[:-1].split(" ")]

#     for case,line in enumerate(f):
#       testcase =
#       ison = (testcase[1]+1)%pow(2,testcase[0])==0
#       if ison:
#         g.write("Case #%d: ON\n"%(case+1))
#       else:
#         g.write("Case #%d: OFF\n"%(case+1))


def simulateThemePark(R,k,groups):
  profit = 0

  peopleon = 0
  numgroups = len(groups)
  runs = 0

  # keep track of where we end in the list, what run that is, how much profit we had
  # for remaining runs, simulate forward from what i we reached
  # total is beforeprofit + modprofit + endprofit
  ends = {}

  realgroupidx = 0
  while True:
    if R == 0:
      break
    i = 0; peopleon = 0
    while True:
      if i == numgroups or peopleon + groups[i] > k:
        break
      else:
        peopleon += groups[i]
        i = i + 1
    groups = groups[i:] + groups[:i]
    profit += peopleon
    runs += 1
    R -= 1
    realgroupidx = (realgroupidx + i) % numgroups

    if (realgroupidx-1) in ends:
#       print "MODDING"
#       print realgroupidx-1
#       print ends[realgroupidx-1]
#       print R
#       print runs

      # if we ever repeat, then mod remaining runs by difference between current run, last time we ended here, multiply by profit gained
      profitperrep = profit - ends[realgroupidx-1][1]
      reps = runs - ends[realgroupidx-1][0]
      cycles = R / reps

#       print profit, reps, profitperrep, cycles
      profit += cycles*profitperrep
      R = (R - cycles*reps) % reps
      ends = {}
    else:
      ends[realgroupidx-1] = (runs,profit)
#   print ends
  return profit, runs

with open(sys.argv[1],'r') as f:
  with open('test.out','w') as g:
    cases = int(f.readline()[:-1]) # number cases
    for j in range(cases):
      R,k,N = parseIntLine(f.readline())
      groups = parseIntLine(f.readline())

      profit, runs = simulateThemePark(R,k,groups)
      g.write("Case #%d: %d\n" % (j+1,profit))

      # mod R and multiply profit
      # simulate remaining cases
      # need to simulate to recurrence twice
