T = int(raw_input())

def cycles(x,c_num,B):
	str_x = str(x)
	counter = 0
	found = []
	for i in xrange(1,c_num):
		new = str_x[i:]+str_x[:i]
		i_new = int(new)
		if x < i_new and i_new <= B and not i_new in found:
			counter+=1
			found.append(i_new)
	return counter

def solve(A,B):
	count = 0
	c_num = len(str(A))
	for i in xrange(A,B+1):
		count+=cycles(i,c_num,B)
	return count
	
for Ti in xrange(1,T+1):
	A,B = [int(x) for x in raw_input().split(' ')]
	print "Case #%d: %d"%(Ti,solve(A,B))
	
