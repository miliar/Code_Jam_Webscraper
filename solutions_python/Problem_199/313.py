import sys

t = int(raw_input())  # read a line with a single integer

ints = []
for i in xrange(1, t + 1):
	raw =raw_input().split()
	s = raw[0]
	k = int(raw[1])# read a list of integers, 2 in this case
	s = list(s)
	ints.append([s, k])
	#print(s)
	#print "Case #{}: {} {}".format(i, n , n )
	
def split(a):
	res = []
	while (a /10) != 0:
		res.append(a % 10)
		a = a/10
	res.append(a)
	return res
	
def sol(lis, k ):
	i = 0
	count = 0
	while i < len(lis):
		if lis[i] == '+':
			i +=1
		else:
			if (i+k) > len(lis):
				return "IMPOSSIBLE"
			lis = flip(lis,k,i)
			count +=1
		
	return count
	

	
def flip(lis, k, index):
	for i in xrange(k):
		if lis[index+i] == '+':
			lis[index+i] = '-'
		else:
			lis[index+i] = '+'
	return lis
	

for i in xrange(t):
	res = sol(ints[i][0],ints[i][1])
	print "Case #{}: {}".format(i+1, res )


# for i in xrange(t):
	# print "Case #{}: {} ".format(i+1, sol(ints[i]) )