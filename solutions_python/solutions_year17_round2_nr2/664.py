t=int(input())
case=1
dic={"v":["r","b"],"g":["y","b"],"o":["r","y"],"r":["r"],"y":["y"],"b":["b"]}
string=str
while t:
	# N, R, O, Y, G, B, and V.
	init=[int(i) for i in input().split()]
	n=init[0]
	lis=[]
	l=["r","o","y","g","b","v"]
	for i in range(6):
		if(init[i+1]!=0):
			lis.append([l[i],init[i+1]])
	str=["x" for i in range(n)]
	i=0;
	str[0]=lis[0][0]
	lis[0][1]-=1
	if(lis[0][1]==0):
		lis.remove(lis[0]);
	j=0;
	#print(lis)
	#while(i<n+10 and j<len(lis) and len(lis)!=0):
	#	if(lis[j][1]==0):
	#		lis.remove(lis[j]);
	#	else:
	for ii in range(1,n):
				if(len(lis)>0):
					for j in range(0,len(lis)):
						if(len(lis)>0 and str[ii]=="x" and not(str[ii-1]=="x" or str[(ii+1)%n]=="x") and (lis[j][0] not in dic[str[ii-1]]) and (lis[j][0] not in dic[str[(ii+1)%n]])):
							str[ii]=lis[j][0];
							lis[j][1]-=1
							if(lis[j][1]==0):
								lis.remove(lis[j]);
						if(len(lis)>0 and str[ii]=="x" and str[ii-1]!="x" and str[(ii+1)%n]=="x" and (lis[j][0] not in dic[str[ii-1]])): 	
							str[ii]=lis[j][0];
							lis[j][1]-=1
							if(lis[j][1]==0):
								lis.remove(lis[j]);
						
				else:
					break;
				#print(lis)
	k=0;
	#print(str)
	#	and (lis[k][0] not in (dic[str[(j+1)%len(str)]]))
	
	if('x' in str):
		temp=str[:str.index('x')]
		for i in range(str.count('x')):
			for j in range(1,len(str)):
				for k in range(len(lis)):
					if(lis[k][0] and str[j]!="x"  and (lis[k][0]not in (dic[str[j]])) and (lis[k][0] not in (dic[str[j-1]])) ):
						tem=str[j:len(str)-1]
						str[j]=lis[k][0];
						str=str[:j]+[str[j]]+tem;
						lis[k][1]-=1
						if(lis[k][1]==0):
										lis.remove(lis[k]);
						if(len(lis)>0):
							break;
	if(len(lis)==0 and ('x' not in str) and (dic[str[0]] not in dic[str[len(str)-1]]) and (dic[str[len(str)-1]] not in dic[str[0]])):
		print("Case #"+string(case)+": "+("".join(str)).upper());
	else:
		print("Case #"+string(case)+": IMPOSSIBLE");
	case+=1
	t-=1
