
T = int( raw_input() )

infty = 1000000000

for t in xrange( 1, T+1 ):
	
	N = int( raw_input() )
	dists = []
	lengths = []
	for i in xrange( N ):
		d, l = map( int, raw_input().split() )
		dists.append( d )
		lengths.append( l )
	
	D = int( raw_input() )
	dists.append( D )
	lengths.append( 0 )
	
	f = [[-infty]*(N+1) for i in xrange(N+1)]
	f[0][0] = dists[0]+min(dists[0],lengths[0])
	best = [-infty]*(N+1)
	best[0] = f[0][0]
	
	for i in xrange( 1, N+1 ):
		for j in xrange( i ):
			if best[j] >= dists[i]: f[i][j] = max( f[i][j], 2*dists[i]-dists[j] )
			f[i][j] = min( f[i][j], dists[i]+lengths[i] )
			best[i] = max( best[i], f[i][j] )
	
	#print best
	print "Case #%d: %s" %(t, "YES" if best[N] >= 0 else "NO")
