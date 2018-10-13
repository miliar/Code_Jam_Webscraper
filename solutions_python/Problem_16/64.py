import sys

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xpermutations(items):
    return xcombinations(items, len(items))

def permute( subs, perm ):
	for n in subs:
		yield ''.join( map( lambda x: n[ perm[ x ] ], range( len( n ) ) ) )

def rle( s ):
	ln = 1
	last = s[0]
	for k in s[1:]:
		if k != last:
			ln+=1
			last = k
	return ln

case=0
cases=int( sys.__stdin__.readline() )
while case < cases:
	case+=1

	k = int( sys.__stdin__.readline() )
	s = sys.__stdin__.readline().rstrip()

	subs = []
	for n in map( lambda x: x*k, range( len( s )/ k ) ):
		subs.append( s[n:n+k] )

	min = -1
	for perm in xpermutations( range( k ) ):
		a = ''.join( permute( subs, perm ) )
		ln = rle( a )
		if( min < 0 ) or ( min > ln ):
			min = ln
	
	print "Case #%d: %d" % ( case, min )

