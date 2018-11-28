import fractions			

def solve(n,queue):
	if n==2:
		return abs(queue[n-1] - queue[n-2])
	temp = range(0,n-1)
	for i in range(0,n-2):
		temp[i] = reduce(fractions.gcd, map(lambda x: abs(x - queue[i]), queue[i+1:]))
		if temp[i]==1:
			return 1
	temp[n-2] = abs(queue[n-1] - queue[n-2])
	return reduce(fractions.gcd, temp)

if __name__ == "__main__":
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	for i in range(1,num+1):
		queue = map(int,f.readline().strip().split(" "))
		n = int(queue[0])
		queue = queue[1:]
		temp = solve(n, queue)
		if temp==1:
			print "Case #%d: %s" %(i,0)
		else:
			if (queue[0] % temp) ==0:
				print "Case #%d: %s" %(i,0)
			else:
				bla = -1*queue[0] + ((queue[0] / temp) +1)*temp
				print "Case #%d: %s" %(i,bla)