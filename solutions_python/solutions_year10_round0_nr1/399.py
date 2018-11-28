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
		print 'Case #%d:'%(t+1)
		inp = f.readline()
		row = inp.split(' ')
		N = int(row[0])
		K = int(row[1])
		#print 'N=',N,',K=',K,
		if (K+1)%(2**N)==0:
			res = 'ON'
		else:
			res = 'OFF'

		fout.write( "Case #%d: %s\n"%(t+1,res) )
	f.close()
	fout.close()