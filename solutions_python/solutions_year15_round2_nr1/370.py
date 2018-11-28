T=int(raw_input())
for t in range(T):
	N=int(raw_input())
	l=len(str(N))
	counter=1
	curr=1
	len_curr=1
	res=None

	if N<=20:
		res=N
	else:
		while len_curr<l:

			if len_curr==1: #1->10
				counter=10

				len_curr+=1
				curr=10**(len_curr-1)
			else:
				right_digits=(len_curr+1)//2
				left_digits=len_curr-right_digits
				counter+=10**right_digits-1 #curr=1009999
				counter+=1 #reverse
				counter+=10**left_digits-1#9999001 --> 10000000 (+999)

				len_curr+=1
				curr=10**(len_curr-1) #10000000

		#len_curr==l
		res=counter+(N-curr)
		right_digits=(len_curr+1)//2
		for i in range(10**right_digits): #10000
			curr+=1
			counter+=1

			reverse=int(str(curr)[::-1])
			if reverse<=N:
				res=min(res,N-reverse+counter+1)

	print "Case #"+str(t+1)+": "+str(res)

