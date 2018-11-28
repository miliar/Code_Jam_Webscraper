import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

def make_it_num( v ):
	for n in range( len(v) ) :
		v[n] = int( v[n] )

def travel(m, ret, h, w, i) :
	global H,W
	while ret[h][w] == 0  :
		ret[h][w] = i
		v = [10000,10000,10000,10000]
		if h != 0 :
			v[3] = m[h-1][w]
		
		if h != (H-1) :
			v[0] = m[h+1][w]
			
		if w != 0 :
			v[2] = m[h][w-1]
		
		if w != (W-1) :
			v[1] = m[h][w+1]
		
		count = 0
		dir = 0
		for d in range(4): 
			if min( v ) == v[d] :
				count = count + 1
				dir = d
		
		#print([h,w,count,dir],v)
		if min(v) < m[h][w] :
			if dir == 3 :
				h = h -1
			elif dir == 2 :
				w = w -1
			elif dir == 1 :
				w = w + 1
			else :
				h = h + 1
		else :
			break
	#print('(',ret[h][w],')')
	return ret[h][w]
	
def solve( ) :
	global pp, code, H, W
	
	v_list = []
	w = ''
	mode = 0;
	m=[]
	for h in range(H):
		l = in_file.readline().strip().split(' ')
		make_it_num( l )
		m.append(l)
	
	ret = [[0 for w in range(W)] for h in range(H)]
	i = 1
	c = 'a'
	list = [' ']
	for h in range(H):
		for w in range(W):
			if ret[h][w] == 0 :
				r = travel( m, ret, h, w, i)
				if r == i :
					#print('=',c)
					list.append( c )
					if c != 'z' :
						c = chr( ord(c) + 1 )
						
				else :
					#print('!',list[r])
					list.append( list[r] )
				i = i + 1
	str = ''
	for h in range(H):
		l=''
		for w in range(W):
			l = l + list[ret[h][w]]  + ' '
		str = str +'\n'+ l
	#pp.pprint(list)
	return str
	

	
ps_time = time.time()
#filename = "test"
#filename = "B-small-attempt0"
filename = "B-large"

in_file = open("./"+filename+".in")
out_file = open("./"+filename+".out","w")

#getting data
T = int(in_file.readline().strip())

for t in range( 1, T+1 ) :	
	v = in_file.readline().strip().split(' ')
	H = int(v[0])
	W = int(v[1])
		
	#solving a problem
	out =  'Case #' + str(t)
	out += ': ' + str( solve() ) + '\n'
	out_file.write( out )
	print (out)

in_file.close()
out_file.close()

ps_time = time.time() - ps_time
print (ps_time)