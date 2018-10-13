import sys

def GCD(a,b):
	# a should not be 0
	if (b==0): return a
	return GCD(b, a%b)
	
def multiGCD( inp ):
	res = []
	for i,p in enumerate(inp):
		res.append( GCD(p, inp[i+1]) )
		if i==len(inp)-2: break
	res.sort()
	return res[0]
	
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
		
		inputs = f.readline().split(' ')
		inp = [ int(i) for i in inputs[1:] ]
		N = len(inp)
		
		inp.sort(reverse=True)
		#print N, inp
		
		#get diff
		diff = []
		for i,p in enumerate(inp):
			diff.append( p-inp[i+1] )
			if i==N-2: break
		#print diff
		#get lcm
		lcm = diff[0]
		if len(diff)>1:
			lcm = multiGCD(diff)
			
		#print lcm
		
		#find the result
		sp = -inp[-1]
		while 1:
			sp+=lcm
			if sp>=0: break
				
		#print sp

		fout.write( "Case #%d: %d\n"%(t+1,sp) )
	f.close()
	fout.close()