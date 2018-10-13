file = "C-small-attempt0.in.txt"

data = [ l.strip().split()  for l in open(file).read().split('\n') ]

lines = int(data[0][0])



for i in xrange(1,lines*2+1,2):
	R = int( data[i][0] ) 
	k = int( data[i][1] ) 
	N = int( data[i][2] )
	
	g = [int(x) for x in data[i+1] ]
	
	earn = 0
	g_i = 0

	for j in xrange(R):
		
		tot = 0
		g_i_start = g_i
		while(1):
			if(tot+g[g_i] > k):
				break
			
			tot = g[g_i]+tot
			g_i = (g_i+1) % N
			
			if(g_i == g_i_start):
				break
	
		earn = earn+tot

	print "Case #%d: %d" % ((i+1)/2,earn)
	