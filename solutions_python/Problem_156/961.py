import fileinput

########################################################
# functions
########################################################
def solve(nu):
	if len(nu)<1:
		return 0
	ma=max(nu)
	if ma<3:
		return ma
	nu.sort()
	a1=[]
	for p in nu:
		if p>1:
			a1.append(p-1)
	a2=nu[:]
	lastval=nu[-1]
	minimi=1+solve(a1)	
	for v in range(2,1+lastval/2):
		a2=nu[:]
		a2[-1]=lastval-v
		a2.append(v)
		t = 1+solve(a2)
		if t<minimi:
			minimi=t
	return minimi
			
				
########################################################
# main
########################################################
f = fileinput.input("B-small-attempt4.in")
T = int(f.readline())
i = 0
for test in range(0,T):
	howmany = int(f.readline())
	arra = f.readline()
	p2 = arra.split(" ")
	p=[]
	for r in p2:
		p.append(int(r))
	i=i+1
	answer=solve(p)
	print "Case #%i: %i"%(i,answer)
	
	

