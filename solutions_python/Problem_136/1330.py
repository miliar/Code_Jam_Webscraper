from __future__ import division
def solve(c,f,x):	
	rate=2
	total=0
	prev=x/rate
	while True:
		prev2=prev
		t1=c/rate
		total+=t1		
		t2=x/(rate+f)
		prev=total+t2		
		if prev>prev2:return prev2	
		rate+=f
fi=open("/home/ashish/Downloads/B1.in","r")
o=open("/home/ashish/Desktop/ans/B1.txt","w")
cases=int(fi.readline().strip())
for i in range(cases):
	#solve
	c,f,x=[float(k) for k in fi.readline().strip().split(" ")]
	o.write("Case #"+repr(i+1)+": %.7f\n"%round(solve(c,f,x),7))
