def is_tidy(n):
	while(n>0):
		if n/10==0:
			return 1
		if n%10 < (n%100)/10:
			return 0
		n /= 10
	return 1

def check(n):
	while(n>0):
		if is_tidy(n)==1:
			return n
		n-=1
	return 0


f = open("test.txt")

t = int(f.readline())

for i in range(1,t+1):
	x = int(f.readline())
	print "Case #"+str(i)+": "+str(check(x))