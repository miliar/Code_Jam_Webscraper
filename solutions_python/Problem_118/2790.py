from numpy import sqrt,ceil,floor
def palind(n):
	if ceil(n)!=floor(n):
		return False
	n=int(n)
	if str(n)==str(n)[::-1]:
		return True
	return False


def count_palind(a,b):
	count=0
	for i in range(a,b+1):
		if palind(i) and palind(sqrt(i)):
			count=count+1
	return count

if __name__=='__main__':
	fp=open("input.txt")
	T=int(fp.readline())
	for i in range(0,T):
		x=fp.readline().strip().split()
		a=int(x[0])
		b=int(x[1])
		print "Case #"+str(i+1)+":",count_palind(a,b)
		
