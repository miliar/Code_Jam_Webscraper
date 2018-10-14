def is_correct(n):
	k = 10
	while(n!=0):
		l = n%10
		if(l>k):
			return 0
		n = n/10
		k = l
	return 1

def prev(n):
	while(not is_correct(n)):
		n-=1
	return n

t = input()
for i in range(t):
	n = input()
	print "Case #" + str(i+1) + ": " + str(prev(n))
