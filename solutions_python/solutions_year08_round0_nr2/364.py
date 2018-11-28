#!/usr/bin/env python

from sys import stdin

ntests = int( stdin.readline() )
for test in xrange( ntests ):
  t = int( stdin.readline() )
  na, nb = map( int, stdin.readline().split() )
  def parse( line ):
    def p( ( h, m ) ): return h * 60 + m
    return [ p( map( int, x.split( ':' ) ) ) for x in line.split() ]
  atimes = [ parse( stdin.readline() ) for i in xrange( na ) ]
  btimes = [ parse( stdin.readline() ) for i in xrange( nb ) ]
  def opp(x): return 'b' if x == 'a' else 'a'
  def events():
    for t0, t1, init in ( [ ( t0, t1, 'a' ) for t0, t1 in atimes ] +
                          [ ( t0, t1, 'b' ) for t0, t1 in btimes ] ):
      yield t0, 'd', init
      yield t1 + t, 'a', opp(init)
  # print '\n'.join( map( str, sorted( events() ) ) )
  present = {'a': 0, 'b': 0}
  req = dict( present )
  for t, ev, loc in sorted( events() ):
    # print t, ev, loc,
    if ev == 'd':
      if present[ loc ] == 0: req[ loc ] += 1; # print '++',
      else: present[ loc ] -= 1
    if ev == 'a': present[ loc ] += 1
    # print
  print 'Case #%d: %d %d' % ( test + 1, req['a'], req['b'] )
