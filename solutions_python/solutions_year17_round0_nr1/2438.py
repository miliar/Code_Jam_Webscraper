t=int(input())
case=1
while case<=t:
	s_=input()
	s_=s_.split(" ")
	k=int(s_[1])
	s=[i for i in s_[0]]
	index=0
	stats=False
	ans=0
	l=len(s)
	while index<l:
		#print(index)
		stats=True
		if s[index]=='-':
			ans = ans + 1
			for i in range(index,index+k):
				if s[i]=='-':
					s[i]='+'
				else:
					s[i]='-'
		x=index
		for i in range(x,l):
			index=i
			if s[i]=='-':
				stats=False
				break
		if index+k>l:
			break
	print("case #",case,":",sep="",end=" ")
	if stats:
		print(ans)
	else:print("IMPOSSIBLE")
	case=case+1
