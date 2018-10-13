#test1
import io 

def swap(s1):
	s2 = []	
	
	for ch in s1:
		if ch == 'a':
			s2.append('y')
		elif ch == 'y':
			s2.append('a')		
		elif ch == 'q':
			s2.append('z')
		elif ch == 'z':
			s2.append('q')
		elif ch == 'd':
			s2.append('s')
		elif ch == 'j':
			s2.append('u')
		elif ch == 'l':
			s2.append('g')
		elif ch == 'm':
			s2.append('l')			
		elif ch == 's':
			s2.append('n')		
		elif ch == 'n':
			s2.append('b')			
		elif ch == 'k':
			s2.append('i')		 
		elif ch == 'r':
			s2.append('t')			
		elif ch == 't':
			s2.append('w')			
		elif ch == 'c':
			s2.append('e')		 			
		elif ch == 'p':
			s2.append('r')			
		elif ch == 'r':
			s2.append('p' )		
		elif ch == 'b':
			s2.append('h')
		elif ch == 'h':
			s2.append('x')
		elif ch == 'x':
			s2.append('m')
		elif ch == 'v':
			s2.append('p')			
		elif ch == 'i':
			s2.append('d')		
		elif ch == 'w':
			s2.append('f')						
		elif ch == 'f':
			s2.append('c')				
		elif ch == 'e':
			s2.append('o')	
		elif ch == 'o':			
			s2.append('k')				
		elif ch == 'g':
			s2.append('v')	
		elif ch == 'u':
			s2.append('j')			
		else:
			s2.append(ch)
	
	return ''.join(s2	)
 
#print 'Output' 
rowC = 0

o = open('output.txt','w')	
i = open('A-small-attempt4.in','r')

for index, line in enumerate(i.readlines()):
	
	if (index==0):
		max = i.readlines()
	if (index>0 and index <max):
		o.write('Case #' + str(rowC) + ': ' + swap(line) )		
	rowC+=1
	
i.close()
o.close()

