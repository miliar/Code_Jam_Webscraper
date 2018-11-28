t=int(input())
case=1
while t:
	d,n=[int(i) for i in input().split()]
	fin=[]
	for i in range(n):
		t1,t2=[int(i) for i in input().split()]
		fin.append((d-t1)/t2);
	m=max(fin);
	ans=d/m;
	
	print("Case #"+str(case)+": "+str(ans));
	case+=1
	t-=1
