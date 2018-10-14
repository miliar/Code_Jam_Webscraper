def ask2(n):
	n=str(n)
	n=list(n)
	for i in range(0,len(n)): n[i] = int(n[i])
	for i in range(len(n)-1,0,-1):
		if n[i]<n[i-1]:
			for j in range(i,len(n)): n[j]=9
			n[i-1]-=1
	res = ""
	for i in n: res += str(i)
	return int(res)
		

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers, 2 in this case
  #print(list(n)," ",m)
  print "Case #{}: {}".format(i, ask2(n))
  # check out .format's specification for more formatting options