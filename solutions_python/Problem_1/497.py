#!/usr/bin/env python
#
# save.py - saves the universe!
#
# Copyright 2008 (C) Mansour Behabadi
#
# NOTE: this is the solution to code.jam contest problem: Save the Universe
#



# main program
if __name__ == '__main__':
   testsCount = int(raw_input())
   # process each test
   for i in xrange(testsCount):
      enginesCount = int(raw_input())
      engines = []
      for j in xrange(enginesCount):
         engines.append(raw_input())
      queriesCount = int(raw_input())
      queries = []
      for j in xrange(queriesCount):
         queries.append(raw_input())
      # do your magic
      minSwitchOps = 0
      checkList = engines[:]
      for q in queries:
         if q in checkList:
            checkList.remove(q)
            if not checkList:
               checkList = [a for a in engines if a != q]
               minSwitchOps += 1
      print "Case #%d: %d" % (i + 1, minSwitchOps)
