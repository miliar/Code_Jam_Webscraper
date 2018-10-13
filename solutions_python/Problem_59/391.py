'''
Created on May 22, 2010

@author: dcasper
'''

from mfw import mfw

infile = 'A-large.in'


with mfw( ( infile, 'r' ), ( '%s.out' % infile[:-3], 'w' ) ) as ( fhi, fho ):

  # 1st line is number of cases.
  cases = int( fhi.readline() )

  for case in range( cases ):
    res = 0

    # N directories exist
    # M need to exist
    N, M = map( int, fhi.readline().split( ' ' ) )

    exists = []

    for i in range( N ):
      exists.append( fhi.readline().rstrip() )

    needed = []

    for i in range( M ):
      needed.append( fhi.readline().rstrip() )

    # Filter out duplicates
    needed = filter( lambda x: x not in exists, needed )

    created = []

    while needed:
      res += len( needed )

      created.extend( needed )

      needed = map( lambda x: x.rpartition( '/' )[0], needed )

      needed = filter( lambda x: x not in created, needed )

      needed = list( set( needed ) )

      needed = filter( lambda x: x is not '', needed )

      needed = filter( lambda x: x not in exists, needed )

    fho.write( 'Case #%d: %d\n' % ( case + 1, res ) )
