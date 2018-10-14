def main():
	T=int(raw_input())
	for case in xrange(T):
		N=int(raw_input())
		x=map(int,raw_input().split())
		print "Case #"+str(case+1)+":",first(N,x),second(N,x)

def first(N,x):
	sum=0
	for i in range(N-1):
		if x[i+1]-x[i] < 0:	sum+=x[i]-x[i+1]
	return sum
	
def second(N,x):
	m=0
	for i in range(N-1):
		m = max(m,x[i]-x[i+1])
	if m<0:	return 0
	sum=0
	for i in range(N-1):
		if x[i]-m < 0 :	sum+=x[i]
		else:			sum+=m
	return sum
	
if __name__=="__main__":
	main()