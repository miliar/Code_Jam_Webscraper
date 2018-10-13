import sys
from sys import stdin

for t in xrange(1, 1+int(stdin.readline().strip())):
	results = []
	wp = []
	owp = []
	oowp = []
	n = int(stdin.readline().strip())
	for z in xrange(n):
		score = stdin.readline().strip()
		results.append(score)
		played=0
		won=0
		for team in score:
			if team != '.':
				played += 1
			if team == '1':
				won += 1
		#print won, played, float(won)/played
		wp.append( (won,played) )
	#print wp
	for z in xrange(n):
		owpnum=0
		owpval=0
		for team in xrange(n):
			if z != team and results[z][team] != '.':
				[theywon, theyplayed] = wp[team]
				if results[z][team]=='0': # we lost against them
					theywon -= 1 # throw away our play
				theyplayed -= 1 # we know they played us
				owpnum += 1
				owpval += float(theywon)/theyplayed
				#print owpval
		owp.append( owpval/owpnum )
	for z in xrange(n):
		oowpnum=0
		oowpval=0
		for team in xrange(n):
			if z != team and results[z][team] != '.':
				oowpnum += 1
				oowpval += owp[team]
		oowp.append( oowpval/oowpnum )
	#print 'wp', wp
	#print 'owp', owp
	#print oowp
	print "Case #{0}:".format(t)
	for z in xrange(n):
	  rpi = .25 * float(wp[z][0])/wp[z][1] + .5 * owp[z] + .25 * oowp[z]
	  print rpi
		
