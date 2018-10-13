import time
import pprint

pp = pprint.PrettyPrinter(indent=4)
def make_it_num( v ):
	for n in range( len(v) ) :
		v[n] = [int( v[n] ),n]

def solve( v ) :
	global pp,D,L,d_list
	
	#pp.pprint (v)
	v_list = []
	w = ''
	mode = 0;
	for c in v :
		if c == '(' :
			w = ''
			mode = 1
		elif c == ')' :
			v_list.append(w[:])
			mode = 0
		elif mode == 1 :
			w = w + str(c)
		else :
			v_list.append(str(c))
	#pp.pprint( v_list )
	
	ret = []
	ret = [0 for n in range(0,D)]
	#pp.pprint( ret )
	for d in range(0,D) :
		for l in range(0,L) :
			#print(d_list[d][l],' in ', v_list[l])
			if v_list[l].find(d_list[d][l]) >= 0	: 
				ret[d] = ret[d] + 1
				#print('!')
	#pp.pprint(ret)
	count = 0
	for d in range(0,D) :
		if ret[d] == L :
			count = count + 1
		
	return count
	

	
ps_time = time.time()
filename = "test"
filename = "A-small-attempt0"
filename = "A-large"

in_file = open("./"+filename+".in")
out_file = open("./"+filename+".out","w")

list = []
#getting data
list = in_file.readline().strip().split(' ')
L = int(list[0])
D = int(list[1])
N = int(list[2])

d_list = []
for d in range( 1, D+1 ) :
	d_list.append( in_file.readline().strip() )

#pp.pprint(d_list)

for n in range( 1, N+1 ) :	
	v1 = in_file.readline().strip()
		
	#solving a problem
	out =  'Case #' + str(n)
	out += ': ' + str( solve(v1) ) + '\n'
	out_file.write( out )
	print (out)

in_file.close()
out_file.close()

ps_time = time.time() - ps_time
print (ps_time)