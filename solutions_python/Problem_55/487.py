from mfw import mfw

infile = 'C-small.in'

with mfw( ( infile, 'r' ), ( '%s.out' % infile[:-3], 'w' ) ) as ( fhi, fho ):

    # 1st line is number of cases.
    cases = int( fhi.readline() )

    for case in range( cases ):
      # First line contains:
      # R - Runs
      # k - Capacity
      # N - Group Count
      R, k, N = map( int, fhi.readline().rstrip().split( ' ' ) )

      # Second line - Groups - N ints, one for each group.
      groups = map( int, fhi.readline().rstrip().split( ' ' ) )

      income = 0

      for i in range( R ):
        currentPassengers = 0

        riding = []

        while len( groups ) and groups[0] + currentPassengers <= k:
          currentPassengers += groups[0]

          riding.append( groups.pop( 0 ) )

        income += currentPassengers

        groups.extend( riding )

      fho.write( 'Case #%d: %d\n' % ( case + 1, income ) )
