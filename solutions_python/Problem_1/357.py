#!/usr/bin/env python

from sys import stdin

ntests = int( stdin.readline() )
for testcase in xrange(ntests):
  nss = int( stdin.readline() )
  ss = [ stdin.readline() for lineno in xrange(nss) ]
  nqs = int( stdin.readline() )
  qs = [ stdin.readline() for lineno in xrange(nqs) ]
  seen = dict( ( s, 0 ) for s in ss )
  def f():
    unseen = set( ss )
    switches = 0
    for q in qs:
      if q in unseen:
        if len( unseen ) == 1: yield list( unseen )[ 0 ]
        unseen.remove( q )
      if len( unseen ) == 0: switches += 1; unseen = set( ss ) - set( [ q ] )
    print 'Case #%d: %d' % ( testcase + 1, switches )
    yield ' '.join( list( unseen ) )
  seq = list( f() )
  #print seq
