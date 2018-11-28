def solve(a,A,b,B):
	print(a,b)
	a-=1
	b-=1
	A=A[a]
	B=B[b]
	count=0;
	for i in range(4):
		for j in range(4):
			if A[i]==B[j]:
				count+=1
				num=A[i]
	if count==0:return "Volunteer cheated!"
	elif count==1:return repr(num)
	else:return "Bad magician!"

f=open("/home/ashish/Downloads/A.in","r")
o=open("/home/ashish/Desktop/ans/A.txt","w")
cases=int(f.readline().strip());
for i in range(cases):
	fans=int(f.readline().strip());
	fmat=[]
	for i1 in range(4):
		fmat.append([int(j) for j in f.readline().strip().split(" ")])
	sans=int(f.readline().strip());
	smat=[]
	for i1 in range(4):
		smat.append([int(j) for j in f.readline().strip().split(" ")])
	o.write("Case #"+repr(i+1)+": "+solve(fans,fmat,sans,smat)+"\n")	
