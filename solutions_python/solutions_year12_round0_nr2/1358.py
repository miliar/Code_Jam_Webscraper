##

# input file caching

with open('/Users/Jerrygao/Desktop/code_jam/large.in','r') as f:
	cin = f.read()

cin = cin.split('\n')

# core algorithm

def ca(cin):
	c = map(int,cin.split(' '))
	N = c[0] # number of dancers
	S = c[1] # suprising results
	p = c[2] # performance level
	T = c[3:] # total points 

	if p != 0 :
		T = filter(lambda x: x!=0, T)
		def_pass = filter(lambda x: x >= p*3, T)
		may_pass = filter(lambda x: p*3 > x >= p*3 -4 ,T)
		ns_pass = filter(lambda x: x >= p*3 -2, may_pass)
		#print len(def_pass),len(may_pass), len(ns_pass), S
		r = len(ns_pass) + S 
		rr = len(may_pass)
		r = len(def_pass)+ (r if rr > r else rr)
	else:
		r = N
	return str(r) 
	
	


# user heuristics

cout=[]

for i in range(1,len(cin)-1):
	out = ca(cin[i]) 
	cout.append('Case #%d: ' % i + out)

cout = '\n'.join(cout)

# output storing  

with open('/Users/Jerrygao/Desktop/code_jam/out.txt','w') as f:
	f.write(cout)

##


