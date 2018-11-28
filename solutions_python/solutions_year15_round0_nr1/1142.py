f=open('A-large.in','r')
out=open('Alarge.txt','w')
n= int(f.readline())
for i in range(1, n+1):
	temp=f.readline().split()
	total=0
	count=0
	people=temp[1]
	for j in range(int(temp[0])+1):
		if int(people[j])>0:
			if total>=j:
				total+=int(people[j])
			else:
				while(total<j):
					total+=1
					count+=1
				total+=int(people[j])
	out.write("Case #"+str(i)+": "+str(count)+"\n")
out.close()
