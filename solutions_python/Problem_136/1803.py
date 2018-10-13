fo = open("out","w")
tc=input()
for i in xrange(1,tc+1):
	c, f, x = map(float,raw_input().split())
	r = 2.0
	tt = 0.00
	while x/r > (x/(r+f)+c/r):
		tt +=c/r
		r=r+f
	tt+=x/r
	tt= "%.7f" %  tt
	fo.write("Case #"+`i`+": "+tt+"\n")
fo.close()