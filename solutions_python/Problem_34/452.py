import sys

class cand:
	def __init__(self, in_str):
		self.cand = []
		for s in in_str:
			self.cand.append(s)
		
		
if __name__=="__main__":
	if len(sys.argv)>1:
		inp = sys.argv[1]
	else:
		print "append an input file param"
		sys.exit()

	f = open( inp, 'rt' )
	output_file = inp.split('.')[0]+"_output.txt"
	fout = open( output_file, 'wt')

	# read header
	header = f.readline()
	headers = header.split(' ')
	L,D,N = int(headers[0]), int(headers[1]), int(headers[2])
	print 'header :', L,D,N

	# read words
	words = []
	for i in range(0,D):
		words.append( f.readline().strip() )

	# read testcases
	for t in range(0,N):
		print 'tc #:', t+1
		tc = f.readline()
		
		parsed = []
		l=n=0
		while n<L:
			#check cands
			if tc[l]!='(':
				#print tc[l]
				parsed.append( cand(tc[l]) )
				l+=1
				n+=1
			else:
				# meets parenthesis (
				end_point = tc[l+1:].find(')')
				#print end_point, tc[l+1:l+end_point+1]
				if end_point<1:
					print 'strange! parsing error occurs!'
				else:
					#ok
					parsed.append( cand(tc[l+1:l+end_point+1]) )
					l+= end_point+2
					n+=1
		
		res = 0
		for word in words:
			c = 0
			for i,w in enumerate(word):
				if w in parsed[i].cand:
					c+=1
			if c>=L:
				res+=1
		print 'Result :', res
		fout.write( 'Case #'+str(t+1)+': '+str(res)+'\n')
	f.close()
	fout.close()