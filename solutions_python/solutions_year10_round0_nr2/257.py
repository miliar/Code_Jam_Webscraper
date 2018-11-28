
def mygcd ( a , b ) :
	while b != 0 :
		t = b ;
		b = a % b ;
		a = t ;
	return a ;

import sys ;

C = sys.stdin.readline() ;
C = C[:len(C)-1] ;
C = int(C) ;
counter = 0 ;
while C > 0 :
	C = C - 1 ;
	counter  = counter + 1 ;
	#print 
	#print 
	#print counter ;
	rnk = sys.stdin.readline() ;
	rnk = rnk[:len(rnk)-1] ;
	rnk = rnk.split( ' ' ) ;
	n = int(rnk[0]) ;
	sgcd = abs(int(rnk[2]) - int(rnk[1])) ;
	#print "sgcd init = ", sgcd ;
	mark = 0 ;
	#print n ;
	if n >= 3 : 
		n = n + 1 ;
		for i in range(3, n ) :
			#print "here in loop "
			sgcd = mygcd ( sgcd, abs(int(rnk[i])-int(rnk[i-1])) ) ;
			#print sgcd ;
			if sgcd == 1 : 
				outputstr = "Case #" + str(counter) + ": 0" 
				print  outputstr ;
				mark = 1; 
				break ;
	if mark == 1 :
			continue ;
	else :
			x= int(rnk[1])%sgcd ;
			if x == 0 : 
				answer = 0 ;
			else :
				answer = sgcd - x ;
				
			outputstr = "Case #" + str(counter) + ": " + str(answer) ; 
			print  outputstr ;

