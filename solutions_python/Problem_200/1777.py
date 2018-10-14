T = int( input() )
for ti in range( 1, T + 1, 1 ):
  N = list( input() )
  ptr = len( N ) - 2
  for i in range( len( N ) - 2, -1, -1 ):
    if ptr < i: continue
    assert( ptr == i )
    if N[ i ] > N[ i + 1 ]:
      while N[ ptr ] == '0':
        ptr -= 1
      N[ ptr ] = chr( ord( N[ ptr ] ) - 1 )
      for j in range( ptr + 1, len( N ), 1 ):
        N[ j ] = '9'
    ptr -= 1
  while len( N ):
    if N[ 0 ] != '0': break
    del N[ 0 ]
  print( "Case #%d: %s" % ( ti, ''.join( N ) ) )
