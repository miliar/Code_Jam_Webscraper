
alphabet = dict()

def parse( input_ , output_ ):

	f = open(input_, 'r')
	g = open(output_, 'r')
	

	L1 = []
	for line in f:
		for col in xrange(len(line)):
			L1.append( line[col] )
	
	L2 = []
	for line in g:
		for col in xrange(len(line)):
			L2.append( line[col] )
	
	for c in xrange( len(L1) ):
		alphabet[ L1[c] ] = L2[c] 
	
	alphabet['z']='q'
	alphabet['q']='z'

	f.close()
	g.close()

def solve( input_, output_ ):
	
	f = open(input_, 'r' )
	g = open(output_,'w' )
	
	T = int( f.readline() )
	
	i=1
	for line in f:
		ans=[]
		ans.append('Case #')	
		ans.append(str(i))
		ans.append(': ')
		sol = ''.join( [alphabet[c] for c in line ] )
		ans.append(sol)
		out = ''.join(ans)
		g.write(out)
		i+=1
	
	f.close()
	g.close()
	
	
def main():

	parse ( './test1.in', './test1.out' )
	solve ( './test2.in', './test2.out' )

if __name__ == '__main__':
    main()
