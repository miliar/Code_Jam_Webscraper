import re,sys
file = sys.argv[1] ;
input = open(file).read().split()  ;
L = int(input[0]) ;
D = int(input[1]) ;
N = int(input[2]) ;
dict = input[3:3+D] ;
pt = input[3+D:3+D+N] ;
T = 1 ;
for p in pt :
	c = 0 ;
	x = re.compile(p.replace("(","[").replace(")","]")) ;
	for d in dict :
		if x.match(d) :
			c += 1 ;
	print "Case #%d: %d" % (T,c) ;
	T += 1 ;
