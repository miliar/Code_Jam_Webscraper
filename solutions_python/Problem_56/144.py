import sys

def check(matrix,N,K):
	B=0
	R=0
	for y in range(0,N):
		for x in range(0,N):
			if matrix[y][x]=='B' or matrix[y][x]=='R':
				bc=0; rc=0
				for i in range(0,K):
					try:
						if matrix[y+i][x]=='B':
							bc+=1
						elif matrix[y+i][x]=='R':
							rc+=1
					except:
						break
				if bc>=K:
					B=1
				if rc>=K:
					R=1
					
				bc=0; rc=0
				for i in range(0,K):
					try:
						if matrix[y+i][x+i]=='B':
							bc+=1
						elif matrix[y+i][x+i]=='R':
							rc+=1
					except:
						break

				if bc>=K:
					B=1
				if rc>=K:
					R=1

				bc=0; rc=0
				for i in range(0,K):
					try:
						if matrix[y][x+i]=='B':
							bc+=1
						elif matrix[y][x+i]=='R':
							rc+=1
					except:
						break
				if bc>=K:
					B=1
				if rc>=K:
					R=1
					
				bc=0; rc=0
				for i in range(0,K):
					try:
						if matrix[y-i][x+i]=='B':
							bc+=1
						elif matrix[y-i][x+i]=='R':
							rc+=1
					except:
						break
				if bc>=K:
					B=1
				if rc>=K:
					R=1					
	if B==0 and R==0:
		return 'Neither'
	elif B==1 and R==0:
		return 'Blue'
	elif B==0 and R==1:
		return 'Red'
	else:
		return 'Both'
	
def rotate(matrix,N,K): 
	#gravity to right side
	
	for y in range(0,N):
		x=N-1
		while x>0:
			if matrix[y][x]=='.' and ( matrix[y].find('R')<x or matrix[y].find('B')<x ):
				matrix[y] = '='+matrix[y][:x] + matrix[y][x+1:]
				continue
				
			x-=1	

	return matrix

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
		
		r1 = f.readline().split(' ')
		N = int( r1[0] )
		K = int( r1[1] )
		#print N,K
		
		matrix = []
		for i in range(0,N):
			l = f.readline().strip()
			matrix.append(l)
		
		matrix = rotate(matrix,N,K)
		res1 = check(matrix,N,K)
			
		#for y in range(0,N):
		#	print matrix[y]
		print res1
		fout.write( "Case #%d: %s\n"%(t+1, res1) )
	f.close()
	fout.close()