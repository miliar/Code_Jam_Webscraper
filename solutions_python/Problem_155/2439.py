T=int(input())
l=[]
for i in range(T):
	x=(str(input()))
	x1=x.split()
	m=int(x1[0])
	v=0
	output=0
	for i in range(len(x1[1])):
		out_i=0
		if v<i:
			out_i=i-v
		v+=int(x1[1][i])+out_i
		output+=out_i
	l.append(output)
for i in range(len(l)):
	print("Case #"+str(i+1)+": "+str(l[i]))