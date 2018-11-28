#magic
fp=open("A-small-attempt0.in","r")
ptr=open("output-P1.txt","w")
num_cases=int(fp.readline())
for i in range(num_cases):
        ans1=int(fp.readline())
	list1=[]
	for j in range(4):
		d=0
		l1temp=(fp.readline()).split()
		l1temp=(map(int,l1temp))
		for d in range(4):
        		list1.append(l1temp[d])

	ans2=int(fp.readline())
	j=0
	list2=[]
	for j in range(4):
		d=0
		l2temp=(fp.readline()).split()
		l2temp=(map(int,l2temp))
		for d in range(4):
        		list2.append(l2temp[d])
        #list2.sort(reverse=True)

        #ind1=list1.index(ans1)
	temp1=ans1-1
	a=[]
	j=0
	#extract that row from list1
	for j in range(4):
		a.append(list1[(temp1*4)+j])
	
	temp2=ans2-1
	b=[]
	#extract that row from list2
	for j in range(4):
		b.append(list2[(temp2*4)+j])

	"""checkrow=[]
	for k in range(4):
		checkrow.append(int(list2.index(a[k])/4))
	checkrow.sort()
	"""
	k=0
	c=0
	for k in range(4):
		if (a[k] in b):
			rightans=a[k]
			c+=1
	if c==1:
		opt=rightans
	elif c>1:
		opt="Bad magician!"
	else:
		opt="Volunteer cheated!"


        ptr.write("Case #{}: {}\n".format(i+1,opt))


         
