import sys
sys.stdin=open('A-large.in','r')
sys.stdout=open('ans','w')
for num in range(input()):
	a,b = raw_input().split()
	a=int(a)
	b = list(b)
	b =map(int,b)
	# print a,b
	prev = b[0]
	ans=0
	for i in range(1,a+1):
		# print i,prev
		if i>prev:
			# print "asd"
			ans+=i-prev
			prev+=i-prev			
		prev+=b[i]
	print "Case #"+str(num+1)+": "+str(ans)
