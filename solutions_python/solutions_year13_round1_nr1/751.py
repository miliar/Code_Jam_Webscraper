#! /usr/bin/python

import sys
_debug_ = False

if 'debug' in sys.argv:
 _debug_ = True


def log(mesg,newline=True):
 if _debug_:
  print mesg,
  if newline: print

input = sys.stdin.readlines()
t = int(input.pop(0))
for c in range(1,t+1):
  (r,v) = ( int(i) for i in input.pop(0).split() )
  log( "r = %d, t=%d"%(r,v) )
  usedpaint=0
  nextr=r
  ringcount=0
  while v > usedpaint:
    nextused = 2*nextr + 1
    if ( usedpaint + nextused > v): break
    else:
      log("ringcount = %d,usedpaint = %d, nextused = %d"%(ringcount,usedpaint,nextused))
      ringcount+=1
      nextr +=  2
      usedpaint += nextused
  print "Case #%d: %d"%(c,ringcount)
