t = int( raw_input() )
for tc in range(0,t):
	n = int( raw_input() )
	nos = raw_input().split(' ')
	sum1 = sum2 = 0
	for i in range(0,n):
		nos[i] = int( nos[i] )
	for i in range(0,n):
		sum1 ^= nos[i]
		sum2 += nos[i]
	nos = sorted( nos )
	ansstr = "Case #" + str( tc+1 ) + ": "
	if sum1 == 0:
		ansstr = ansstr + str( sum2 - nos[0] )
	else:
		ansstr = ansstr + "NO"
	print ansstr
