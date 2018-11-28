def worth(curr, prod, coss, incr, goaa):
	return (((coss-curr)/(prod) + goaa/(prod+incr)) < (goaa-curr)/(prod))


def optimal(cost, increase, goal):
	current = 0.0
	production = 2.0
	time = 0.0
	for i in range(100000):
		if(worth(current, production, cost, increase, goal)):
			time+=(cost-current)/(production)
			current = cost				
			current-=cost 
			production+=increase
		else:
			time+=(goal-current)/(production)
			return time

T = int(raw_input())
for t in range(T):
	s = raw_input()
	row = [float(elem) for elem in s.split()]			
	c = row[0]
	f = row[1]
	x = row[2]
	print "Case #" + str(t+1) + ":", optimal(c,f,x)	


		
