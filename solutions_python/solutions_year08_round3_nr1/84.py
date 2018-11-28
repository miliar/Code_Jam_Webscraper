import time

def make_it_num( v ):
	for n in range( len(v) ) :
		v[n] = int( v[n] )

def make_it_num2( v ):
	for n in range( len(v) ) :
		v[n] = [int( v[n] ),n]
		
def solve( p,k,l,freq ) :
	print p,k,l
	print freq
	freq.sort()
	freq.reverse()
	print freq
	
	if len( freq ) > k*p : return 'Impossible'
	c = 0;
	sum = 0;
	pad = []
	for ip in range( p ):
		pad.append( [] )
		for ik in range( k ):
			pad[ip].append( freq[c][1] )
			sum += freq[c][0] * (ip+1)
			c += 1
			if c >= len( freq ) : break
		if c >= len( freq ) : break
			
	#for ip in range( p ):
	#	print pad[ip]
	
	
	return str( sum )
	

	
ps_time = time.time()
filename = "test"
filename = "A-small-attempt0"
filename = "A-large"

in_file = file("./"+filename+".in")
out_file = file("./"+filename+".out","w")

total_case_num = int( in_file.readline() )
for case_num in range( 1,total_case_num+1 ) :
	#initial
	
	#getting data
	line = in_file.readline().strip()
	data = line.split(' ')
	make_it_num( data )
	p, k, l = data
	
	line = in_file.readline().strip()
	freq = line.split(' ')
	make_it_num2( freq )
		
	#solving a problem
	out =  'Case #' + str(case_num)
	out += ': ' + str( solve(p,k,l,freq) ) + '\n'
	out_file.write( out )
	print out

in_file.close()
out_file.close()

ps_time = time.time() - ps_time
print ps_time