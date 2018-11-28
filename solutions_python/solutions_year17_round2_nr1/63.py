T = int( input() )
for ti in range( 1, T + 1, 1 ):
  D, N = map( int, input().split() )
  K = []
  S = []
  for i in range( N ):
    k, s = map( int, input().split() )
    K.append( k )
    S.append( s )
  lb, ub = 0.0, 1e30
  for i in range( 200 ):
    mid = ( lb + ub ) / 2
    ng = False
    for i in range( 0, N ):
      if mid <= S[ i ]: continue
      if K[ i ] / ( mid - S[ i ] ) >= ( D - K[ i ] ) / S[ i ]: continue
      ng = True
      break
    if ng:
      ub = mid
    else:
      lb = mid
  print( "Case #%d: %.7f" % ( ti, lb ) )
