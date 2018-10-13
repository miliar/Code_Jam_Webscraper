a=open("input1","r").read()
a=a.split("\n")
cases=int(a[0])
a=a[1:-1]
for i in range(len(a)):
	a[i]=a[i].split(" ")
f=0
out=open("out","w")
while(f<cases and len(a)>9):
	in1=a[:5]
	a=a[5:]
	in2=a[:5]
	a=a[5:]
	row1=int(in1[0][0])-1
	in1=in1[1:]
	row2=int(in2[0][0])-1
	in2=in2[1:]
	ans=list(set(in1[row1]).intersection(in2[row2]))
	if len(ans)==1:
		out.write ("Case #"+str(f+1)+": "+ans[0]+"\n")
	if len(ans)==0:		
		out.write ("Case #"+str(f+1)+": Volunteer cheated!\n")
	if len(ans)>1:
		out.write ("Case #"+str(f+1)+": Bad magician!\n")
	f=f+1
out.close()
