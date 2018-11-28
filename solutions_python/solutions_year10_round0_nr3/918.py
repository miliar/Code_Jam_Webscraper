from sys import stdin,stdout


def case(R,k,list):
	total = 0
	pos = 0
	listL = len(list)
	for t in range(R):
		capacity = k
		groups = 0
		while(capacity >= list[pos] and groups <listL):
			total = total + list[pos]
			capacity = capacity - list[pos]
			pos = (pos+1)%listL
			groups = groups +1
	return total

num = int(stdin.readline())
for i in range(0,num):
	R,k,total = map( lambda x: int(x), stdin.readline().split())
	list = map( lambda x: int(x), stdin.readline().split())
	result = case(R,k,list)
	print "Case #%d: %d"%(i+1,result)


