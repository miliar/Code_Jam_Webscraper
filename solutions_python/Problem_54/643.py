
f = open("B-small-attempt0.in","r")
out = open("B-small.out","w")
T = int(f.readline())
C=0
def gcd(a,b):
	if a>b:
		a,b = b,a
	while(b>0):
		a,b = b,a%b
	return a
for i in f:
	C+=1
	s = [ int(elem) for elem in i.split()[1:]]
	div= abs(s[0] - s[1])
	for x in xrange(1,len(s)-1):
		div = gcd(div,abs(s[x]-s[x+1]))
	temp = s[0]
	while (temp>0):
		temp -= div
	out.write("Case #"+str(C)+": "+str(abs(temp))+"\n")
	if C==T:
		break

out.close()
f.close()

