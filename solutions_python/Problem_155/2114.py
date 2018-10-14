#inp = open("a.text","r")
#inp = open("..\..\A-small-attempt0 (4).in","r")
inp = open("..\..\A-large (1).in","r")
outp = open("out.text","w")

n = int(inp.readline())

line = inp.readline()
idx = 0


while line:
	a,b = line.split()
	res = 0
	idx += 1
	sum = 0
	for i in range(int(a)+1) :
		if ( i > sum + res ) : res += i-(sum+res)
		sum += int(b[i]) 

	outp.write("Case #%d: %d\n" % ( idx, res) )
	line = inp.readline()