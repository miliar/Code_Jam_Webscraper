

t = int( input() )

for testcase in range (1, t+1):
	
	odpoved=0
	ac, aj = [int(x) for x in input().split() ]
	usek = []
	cameron = 0
	jamie = 0
	for i in range (ac):
		c, d = [int(x) for x in input().split() ]
		usek.append( (c,d,'J') )
		jamie += d-c
	for i in range (aj):
		j, k = [int(x) for x in input().split() ]
		usek.append( (j, k, 'C') )
		cameron += k-j
	
	usek = sorted(usek)
	#print(usek)
	
	jamieusek = []
	cameronusek = []
	zmiesanyusek = []
	
	for i in range( 0, ac+aj-1 ):
		if usek[i][2]=='J' and usek[i+1][2] == 'J':
			jamieusek.append( usek[i+1][0] - usek[i][1] )
		elif usek[i][2] == 'C' and usek[i+1][2] == 'C':
			cameronusek.append ( usek[i+1][0] - usek[i][1] )
		else:
			zmiesanyusek.append( usek[i+1][0] - usek[i][1] )
			
	if usek[ac+aj-1][2]=='J' and usek[0][2] == 'J':
		jamieusek.append( usek[0][0] + 60*24 - usek[-1][1] )
	elif usek[ac+aj-1][2] == 'C' and usek[0][2] == 'C':
		cameronusek.append ( usek[0][0] + 60* 24 - usek[-1][1] )
	else:
		zmiesanyusek.append ( usek[0][0] + 60* 24 - usek[-1][1] )
	
	jamieusek = sorted( jamieusek, reverse = True )
	cameronusek = sorted( cameronusek, reverse = True )
	
	if jamie + sum(jamieusek) > 12*60:
		while jamie + jamieusek[-1] <= 12*60:
			jamie += jamieusek[-1]
			jamieusek.pop()
		odpoved += 2*len(jamieusek)
	
	if cameron + sum(cameronusek) > 12*60:
		while cameron + cameronusek[-1] <= 12*60:
			cameron += cameronusek[-1]
			cameronusek.pop()
		odpoved += 2*len(cameronusek)
	
	odpoved += len(zmiesanyusek)
	
	print ("Case #{0}: {1}".format(testcase, odpoved) ) 