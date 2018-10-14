def recycle(A, B):
	s = str(A)
	l = len(s)

	if(l <= 1):
		return 0
	
	n = A
	out = []
	
	while(n <= B):
		i = -1
		while(i > -1 * l):
			m = str(n)[i:] + str(n)[:i]
			i -= 1
			key = int(m + str(n))
			key2 = int(str(n) + m)
			if(m[0] != '0' and int(m) != int(n) and int(m) > A and int(m) < B and key not in out):
				#print m,n
				out.append(key)
				out.append(key2)
		n += 1
	
	return len(out)/2
	


f = open('C-small-attempt2.in', 'r')
T = int(f.readline())
for i in range(T):
	nums = f.readline().split(' ')
	A = int(nums[0])
	B = int(nums[1])
	#print (A,B)
	print "Case #{}: {}".format(i+1, recycle(A,B))