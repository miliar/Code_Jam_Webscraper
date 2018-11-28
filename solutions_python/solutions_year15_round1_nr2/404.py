file_name='B-small-attempt1.in'
from functools import reduce
from fractions import gcd
# Note: these two fucntions are downlaoded from the web.
def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(l):
    """Return lcm of args."""   
    return reduce(lcm, l)

def firstZero(w,M):
	minimum=-1
	index=-1
	for i in range(len(w)):
		if  minimum>w[i] or minimum==-1:
			minimum=w[i]
			index=i
	w[index]+=M[index]
	return index

f=open(file_name,'r')
T=eval(f.readline())
result=open('b.out','w')
for t in range(T):
	# print('testing case '+str(t+1))
	[B, N]=f.readline().split()
	B=eval(B)
	N=eval(N)
	M=list(map(eval,f.readline().split()))
	w=[0]*B


	if B>=N:
		result.write('Case #'+str(t+1)+': '+str(N)+'\r')
		continue
	d=lcmm(M)
	c=sum(map(lambda x:d//x,M))
	for i in range(N%c+c):
		index=firstZero(w,M)

	result.write('Case #'+str(t+1)+': '+str(index+1)+'\r')
	
f.close()
result.close()