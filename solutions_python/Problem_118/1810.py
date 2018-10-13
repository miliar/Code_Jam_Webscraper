import math
import re
g=[]
palindrome_list=[0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321,400000080000004]
def readInput():
	global output,g
	f = open('C-large-1.in', 'r')
	count = f.readline()

	for num in range(1,int(count)+1):		
		br = f.readline()
		str1=re.findall(r'\d+', br)
		g=g+[[long(str1[0]),long(str1[1])]]
	print g;
	#o=''.join(g).replace('\n','')
def processCase(case):
	count =0
	#print case
	for pal in palindrome_list:
		#print pal,case[0], case[1]
		#print pal> case[0] and pal<case[1]
		if pal>= case[0] and pal<=case[1]:
			count =count +1
	return str(count)
			
def printOutput():
	global g
	fo = open('output_large.txt', 'w')
	for k,case in enumerate(g):
		fo.write('Case #'+str(k+1)+': '+processCase(case)+'\n')	
		
def is_palindrome( int_in_question) :
    as_list_of_chars = list( str( int_in_question))
    reversed_list_of_chars = list( as_list_of_chars)
    reversed_list_of_chars.reverse( )
    return as_list_of_chars == reversed_list_of_chars

def print_palindrome_squares_up_to(limit) :
	i=0
	while i<limit:
		if is_palindrome( i) and is_palindrome( i * i) :
			print( i, str(i * i))
		i=i+1

#print_palindrome_squares_up_to(long(math.pow(10,10)))

readInput()
printOutput()