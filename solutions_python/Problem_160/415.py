from sys import argv 

def lcm(x,y):
    tmp=x
    while (tmp%y)!=0:
        tmp+=x
    return tmp

def lcmm(*args):
    return reduce(lcm,args)

T=int(raw_input())
for i in range(T):
	B,N=map(int, raw_input().split())
	# print B, N
	args= []

	args=map(int, raw_input().split())
	barbor_occupy= [0 for x in range(len(args))]	
	a = lcmm(*args)
	add=0
	for z in range(len(args)):
		add+=a/args[z] 
	N=N%add
	print N ,add
	l=0
	count=0
	while count!=N:
		l=barbor_occupy.index(min(barbor_occupy))
		barbor_occupy[l]+=args[l]
		count+=1
	print barbor_occupy
	print count
	if N == 0:
		l=len(args)-1
	print "Case #%d: %d"%(i+1,l+1)


