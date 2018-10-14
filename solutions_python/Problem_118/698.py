f=open("C-large-1.in","r")
g=open("C-large-1.out","w")
def isPalindrome(x):
	p=x
	l=[]
	while(p>0):
		b=p%10
		p/=10
		l.append(b)

	for i in xrange(len(l)):
		if l[i]!=l[len(l)-1-i]:
			return False
	return True
#Palindrome List
# Palin=[]
# for i in xrange(1,10000000):
# 	if isPalindrome(i) and isPalindrome(i*i):
# 		Palin.append(i)
# print Palin,len(Palin)
palin=[1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 
10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 
101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 
1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 
2000002, 2001002]
palinSq=[x*x for x in palin]

#[A,B]
T=int(f.readline())
for t in xrange(1,1+T):
	line=f.readline().split()
	line=[int(x) for x in line]
	A=line[0]
	B=line[1]
	a=len([i for i in palinSq if i<A])
	b=len([i for i in palinSq if i<=B])
	g.write("Case #"+str(t)+": "+str(b-a)+'\n')
f.close()
g.close()