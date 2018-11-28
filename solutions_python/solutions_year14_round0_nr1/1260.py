f=open('A-small-attempt0.in','r')
f2=open('Asmall.out','w')

numTest=int(f.readline())

for i in range(0,numTest):
	ans1=int(f.readline())
	arr1=[]
	for x in range(0,4):
		arr1.append(f.readline())
	row1=arr1[ans1-1].split()


	ans2=int(f.readline())
	arr2=[]
	for x in range(0,4):
		arr2.append(f.readline())
	row2=arr2[ans2-1].split()

	count=0

	for x in range(0,4):
		if row2[x] in row1:
			output=row2[x]
			count+=1

	if count>1:
		output="Bad magician!"
	else:
		if count==0:
			output="Volunteer cheated!"

	f2.write("Case #"+str(i+1)+": "+str(output)+"\n")

