for T in range(input()):
 x=raw_input().split();t=i=1;w=[1,1];d=[0,0]
 while i<len(x):
	c=x[i]<"F";v=int(x[i+1])
	if abs(w[c]-v)<=d[c]:i+=2;w[c]=v;d[c]=-1
	d[0]+=1;d[1]+=1;t+=1
 print"Case #%s:"%(T+1),t-1