def printfun(inp,i,val):
	print "{}	case #{}: {}".format(inp,i,val)

def check(x):
	global flag
	t = []
	for i in xrange(len(x)-1):
		if int(x[i]) > int(x[i+1]):
			x = x[:i]+str(int(x[i])-1)+(len(x)-i-1)*"9"
			return x	
		else:			
			t.append(1)
	flag = all(t)
	return x


t = raw_input()
print "Number of Test Case: "+t
print "\nInput   Output"
t = int(t)


for i in xrange(1, t+1):
	flag = False
	inp = raw_input()
	temp = inp
	if len(inp) == 1:
		printfun(inp,i,temp)
	else:
		val = temp
		while(flag == False):
			val = check(val)
		printfun(inp,i,int(val))
