N=int(input())
n=N
while n:
	num=list(input())
	done=0
	maxlen=len(num)
	cur=maxlen-1
	while cur:
		# print("if "+num[cur]+"<"+num[cur-1])
		if int(num[cur])<int(num[cur-1]):
			num[cur-1]=str(int(num[cur-1])-1)
			tmp=cur
			while tmp<maxlen:
				num[tmp]='9'
				tmp=tmp+1
		# print("num="+''.join(num))
		# print("cur="+str(cur))
		cur=cur-1
		'''
		if cur==0:
			if ''.join(num)==''.join(sorted(num)):
				done=1
				print("Case #"+str(N-n+1)+": "+str(num))
			else:
				cur=maxlen
		'''
	print("Case #"+str(N-n+1)+": "+str(int(''.join(num))))
	n=n-1
'''
while n:
	num=input()
	done=0
	while not(done):
		if num==''.join(sorted(list(num))):
			done=1
			print("Case #"+str(N-n+1)+": "+str(num))
		num=str(int(num)-1)
	n=n-1
'''