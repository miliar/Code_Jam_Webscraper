t = input()
s = t
ans = ""
while(t):
	n, a = raw_input().split()
	n = int(n)
	sum = 0
	reqd = 0
	for x in xrange(n+1):
		if (sum < x and int(a[x]) > 0 ):
			reqd = reqd + x-sum
			sum = sum+reqd+int(a[x])
			print reqd
		else:
			sum += int(a[x])
	ans += "Case #"+ str(s-t+1) + ": " + str(reqd) +"\n"
	t-=1
print ans