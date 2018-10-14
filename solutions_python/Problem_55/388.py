import sys

if __name__=="__main__":
	if len(sys.argv)>1:
		inp = sys.argv[1]
	else:
		print "append an input file param"
		sys.exit()

	f = open( inp, 'rt' )
	nTC = int( f.readline() )
	print 'the number of tc :', nTC

	output_file = inp.split('.')[0]+"_output.txt"
	fout = open( output_file, 'wt')

	for t in range(0, nTC):
		print 'Case #%d'%(t+1)
		inp = f.readline().split(' ')
		R = int(inp[0])
		k = int(inp[1])
		N = int(inp[2])
		
		inp2 = f.readline().split(' ')
		g = [ int(i) for i in inp2 ]
			
		#print R, k, N
		#print g
		
		ids = []
		i = 0
		cap = 0
		run = 0
		earn = 0
		while 1:
			cap += g[i]
			if cap>k or i in ids:
				run += 1
				earn += cap-g[i]
				cap = 0
				i-=1
				#print run, earn, ids
				ids=[]
				if run==R: break					
			ids.append(i)
			i+=1
			if (i==len(g)): 
				i=0
		
		print earn
		fout.write( "Case #%d: %d\n"%(t+1, earn) )
	f.close()
	fout.close()