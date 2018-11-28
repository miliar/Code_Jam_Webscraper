def numSpinner( m ):
	if ( len(m) <= 1 ):
		return m
	else:		
		return ( m[len(m)-1] + m[0:(len(m)-1)] )


t = int ( raw_input() )
for i in range(t):
	count = 0
	AnB = raw_input()
	AnB = AnB.split()
	a = int ( AnB[0] )
	b = int ( AnB[1] )
	for j in range( a, (b+1) ):
		strJ = str( j )
		strTemp = numSpinner( strJ )
		while ( strJ != strTemp):
			temp = int(strTemp)
			if( (a <= temp) and (temp <= b)  and (temp != j) ):
				count += 1
			strTemp = numSpinner( strTemp )
	print ( "Case #"+ str(i+1) + ": " + str( count / 2 ) )
