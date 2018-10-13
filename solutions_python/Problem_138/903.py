input_file = "d2.in"
infile = open(input_file)

lines = infile.readlines();
t = int( lines[0] )
lines = lines[ 1: ]
for i in range( t ):
	print "Case #" + str(i+1) + ": ",
	numBlks =int( lines[ (i*3)  ].rstrip() )
	# handle Naomi
	naomiBlks = lines[ (i*3) +1 ].rstrip()
	naomiBlks = [float(x) for x in naomiBlks.split(" ")]
	naomiBlks.sort( reverse=True )
	# handle Ken
	kenBlks = lines[(i*3 ) + 2 ].rstrip()
	kenBlks = [float(x) for x in kenBlks.split(" ")]
	kenBlks.sort()
	nb = naomiBlks[:]
	kb = kenBlks[:]
	# Deceitful War
	y = 0
	nb.sort()
	for i in nb:
		pending = True
		for j in kb:
			if pending and ( i > j ):
				  kb.remove(j)
				  pending = False
		if pending:
			y += 1
			kb.remove( kb[-1] )
	y = numBlks - y
	# War
	z = 0
	for i in naomiBlks:
		pending = True
		for j in kenBlks:
			if pending and (j > i):
				  kenBlks.remove(j)
				  pending = False
		if pending:
			z += 1
			kenBlks.remove( kenBlks[0] )
	print str(y)+" "+str(z)
	
#if tn > ck :
#	if cn > ck

