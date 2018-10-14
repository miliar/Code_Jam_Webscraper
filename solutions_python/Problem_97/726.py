
# Learning Python #

def show( g, test, ans ):
		res=[]
		res.append('Case #'+str(test)+': '+str(ans)+'\n')
		g.write(''.join(res))

def solve( input_, output_ ):
	
	f = open(input_, 'r' )
	g = open(output_,'w' )
	
	T = int( f.readline() )
	
	t=0
	for line in f:
		line = line.split(' ')		
		
		A = int(line[0])
		B = int(line[1])
		
		d = dict()
		i=A
		ans = 0
		while i<=B:
			
			c = i
			l = []
			
			l = [ c[i] for i in xrange(c) ]
			
			j=len(l)-1
			while j > 0:
				
				sol = l[j:len(l)] + l[0:j] 
				sol = int( ''.join(sol) ) 
			
				if sol >= A and sol <= B and sol>i:
					d[(sol,i)]=0	
				
				j-=1
			
			i+=1
		t+=1
		
		show( g, t, len(d.keys()) )
		
def main():
	solve ( './test1.in', './test1.out' )

if __name__ == '__main__':
    main()
