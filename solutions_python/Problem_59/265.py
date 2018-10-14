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
		
		inp = f.readline().strip().split(' ')
		N = int(inp[0])
		M = int(inp[1])
		#print N,M
		
		#created
		fs = []
		for i in range(0,N):
			name = ''
			for inp in f.readline().strip().split('/'):
				if len(inp)<1: continue
				name+='/'+inp
				if name not in fs:
					fs.append( name )
		#print fs
		
		#to create
		cnt = 0
		for i in range(0,M):
			name = ''
			for inp in f.readline().strip().split('/'):
				if len(inp)<1: continue
				name+='/'+inp
				if name not in fs:
					cnt+=1
					fs.append( name )
					
		#print cnt
		fout.write( "Case #%d: %d\n"%(t+1, cnt) )
	f.close()
	fout.close()