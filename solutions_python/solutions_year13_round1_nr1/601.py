import math
test=input()
p1=test
while(test>0):
    x=raw_input()
    y=x.split()
    r=int(y[0])
    t=int(y[1])
    p=1+(2*r)
    p=p-2
    d=p*p*1.0
    d=d+(8*t)
    d=math.sqrt(d)
    d=d-p
    d=d/4.0
    a=int(math.floor(d))
    while((2*a*a + (2*r -1)*a)>t):
	a=a-1
    s='Case #'+str(p1-test+1)+': '+str(a)
    print s
    test=test-1
