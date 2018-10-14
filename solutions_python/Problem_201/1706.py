from queue import PriorityQueue

T = int( input() )
for ti in range( 1, T + 1, 1 ):
  N, K = map( int, input().split() )
  pq = PriorityQueue()
  pq.put( [ - ( N - 1 >> 1 ), - ( N >> 1 ), 0, N ] ) # [ lb, rb )
  ans_l, ans_r = -1, -1
  while not pq.empty() and K:
    mi, mx, lb, rb = pq.get()
    mi *= -1
    mx *= -1
    ans_l, ans_r = mx, mi
    mid = lb + ( rb - lb - 1 ) // 2
    if mid - lb > 0:
      n = mid - lb
      pq.put( [ - ( n - 1 >> 1 ), - ( n >> 1 ), lb, mid ] )
    if rb - ( mid + 1 ) > 0:
      n = rb - ( mid + 1 )
      pq.put( [ - ( n - 1 >> 1 ), - ( n >> 1 ), mid + 1, rb ] )
    K -= 1
  print( "Case #%d: %d %d" % ( ti, ans_l, ans_r ) )
