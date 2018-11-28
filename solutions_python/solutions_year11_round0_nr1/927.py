t = int( raw_input() )

for tc in range(0,t):
	bt = ot = 0
	bp = op = 1
	st = raw_input().split(' ')
	n = int(st[0])
	x = 1
	while n:
		n-=1
		ch = st[x]
		x+=1
		no = int(st[x])
		x+=1

		if ch == 'B':
			tmp = abs( no - bp )
			bt = max( bt + tmp, ot ) +1
			bp = no
		else:
			tmp = abs( no - op )
			ot = max( ot + tmp, bt ) + 1
			op = no
	print "Case #" + str(tc+1) + ": " + str(max( ot, bt ))
