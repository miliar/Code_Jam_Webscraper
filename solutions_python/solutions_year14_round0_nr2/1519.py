import sys
sys.setrecursionlimit(100000)

def f():
	with open("input.txt","r") as read:
		with open("output.txt","w")as write:
			case = read.readline()
			for j in range(int(case)):
				c,f,x = [float(i) for i in read.readline().split()]
				#print c,f,x
				x=ff(c,f,x,2,0)
				write.write("Case #"+str(j+1)+ ": %.7f" % x+"\n")
		write.close()
	read.close()


def ff(c,f,x,r,t):
	'''
	if x < c+1:
		return 1
	if r >x:
		return x;
	notake = x/r
	take = ff(c,f,x,r+f)+c/r
	return min(notake,take)
	'''
	while True:
		ct = x/r
		nr = r+f
		et = c/r + x/nr
		if ct < et:
			t+=ct
			return t
		else:
			t+=c/r
			r = nr

print f()
