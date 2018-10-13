T = int( input() )
for ti in range( 1, T + 1, 1 ):
  S, K = map( str, input().split( ' ' ) )
  S = list( S )
  K = int( K )
  ans = 0
  for i in range( len( S ) - K + 1 ):
    if S[ i ] == '+': continue
    ans += 1
    for j in range( i, i + K, 1 ):
      if S[ j ] == '+':
        S[ j ] = '-'
      else:
        S[ j ] = '+'
  for i in range( len( S ) ):
    if S[ i ] == '-':
      ans = -1
      break
  if ans == -1:
    print( "Case #%d: IMPOSSIBLE" % ti )
  else:
    print( "Case #%d: %d" % ( ti, ans ) )
