a=input()
for i in xrange(a):
	m=list()
	for j in xrange(4):
		m+=[raw_input()]
	raw_input()
	m+=[m[0][0]+m[1][1]+m[2][2]+m[3][3]]
	m+=[m[0][3]+m[3][0]+m[1][2]+m[2][1]]
	for j in xrange(4):
		m+=[m[0][j]+m[1][j]+m[2][j]+m[3][j]]

	if ('XXXX' in m or 'XXXT' in m or 'XXTX' in m or 'XTXX' in m or 'TXXX' in m ):
		print "Case #"+str(i+1)+": X won"
	elif ('OOOO' in m or 'OOOT' in m or 'OOTO' in m or 'OTOO' in m or 'TOOO' in m ):
		print "Case #"+str(i+1)+": O won"
	elif ('.' in m[0] or '.' in m[1] or '.' in m[2] or '.' in m[3]):
		print "Case #"+str(i+1)+": Game has not completed"
	else:
		print "Case #"+str(i+1)+": Draw"

