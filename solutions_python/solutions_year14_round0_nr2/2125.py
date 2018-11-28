def ints():
    return map(int, raw_input().split())
def floats():
	return map(float, raw_input().split())

T=int(raw_input())
for tt in range(T):
	c,f,x = floats()
	#print c,f,x
	res=10000000000
	tcosts=[0] # time to build the kth farm
	sumsofar=0.0
	#print tt,'here'
	for i in range(int(x+1)):
		sumsofar+=f*tcosts[-1]
		tk=((i+1)*c+ sumsofar)/(2+i*f) #i.e. we see how much time it takes to build the kth farm
		tcosts.append(tk)
		t=(x+i*c+sumsofar)/(2+i*f) #then it takes 2T + f(T-t0) + f(T-t1) + ... = x+ k*f . Now solve for T
		#print t
		if t<res:
			res=t
		else:
			break #exceeded number needed
		
	print 'Case #%d: %.7f'%(tt+1,res)