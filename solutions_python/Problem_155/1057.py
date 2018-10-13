f=open("A-large.in","r")
f2=open("output.out","w")
data=f.read().splitlines()
c=int(data[0])
result=""
num=0
line =1
su=0
for i in range(c):
	temp=data[line].split(" ")
	n=int(temp[0])
	ham=temp[1]
	for j in range(n+1):
		#print j, int(ham[j]),su
		temp2=int(ham[j])
		if (temp2 >0):
			if (j<=su):
				su+=temp2
			else:
				num+=(j-su)
				su+=(j-su)
				su+=temp2
		
	result+="Case #"+str(i+1)+": "+str(num)+"\n"
	num=0
	line+=1
	su=0
	temp2=0
#print result
f2.write(result)
f2.close()