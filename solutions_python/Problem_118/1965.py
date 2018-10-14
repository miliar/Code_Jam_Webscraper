import math
def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return int(root)
    else:
        return 0
def palindrome(L):
    return L == L[::-1]
    
f=open('C-small-attempt0.in')
T=int(f.readline())
g=open('output','wa')
for i in range(0,T):
	AB=f.readline().split()
	AB = map(int, AB)
	A=AB[0]
	B=AB[1]
	c=0
	for k in range(A,B+1):
		p=is_square(k)
		if(p!=0 and palindrome(str(k)) and palindrome(str(p))):
			c=c+1		

	g.write('Case #'+str(i+1)+': '+str(c)+'\n')
	
	
