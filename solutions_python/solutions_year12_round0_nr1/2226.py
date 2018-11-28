import sys

mapping = { 'a' : 'y' , 'b' :'h' ,'c' :'e' ,'d':'s' ,'e':'o' ,'f':'c' ,'g':'v' ,'h':'x' , 'i':'d','j':'u', 'k':'i', 'l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q', ' ':' ' ,'\n':'' }
#print "size is ",len(mapping)
n = int(sys.stdin.readline())

for i in range( 1,n+1 ) :
	soln = ''	
	words = sys.stdin.readline()#.split()
	for letter in words :
		soln += mapping[ letter ]

	print "Case #%d: %s"%( i,soln )
