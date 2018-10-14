
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
		
		N = int(line[0])
		S = int(line[1])
		P = int(line[2]) 
		
		M1 = P*3-2
		M2 = P*3-4
		
		i=3
		ans=0
		
		while i < len(line):
			val = int(line[i])
			i+=1
			
			if val < P:
				continue
		
			if val >= M1:
				ans+=1
				continue
				
			elif val >= M2 and S > 0:
			 	ans+=1
			 	S-=1
		
		t+=1
		show(g,t,ans)
		
	f.close()
	g.close()	

def main():
	solve ( './test1.in', './test3.out' )

if __name__ == '__main__':
    main()
