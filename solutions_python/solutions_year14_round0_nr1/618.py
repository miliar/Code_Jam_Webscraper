fp=open("A-small-attempt0.in","r")
ptr=open("output.txt","w")
num_cases=int(fp.readline())
for i in range(num_cases):
        ans1=int(fp.readline())
	l1=[]
	list1=fp.readline().split()
	list1=map(int,list1)
	l1.append(list1)
        list1=fp.readline().split()
	list1=map(int,list1)
	l1.append(list1)
        list1=fp.readline().split()
	list1=map(int,list1)
	l1.append(list1)
        list1=fp.readline().split()
	list1=map(int,list1)
	l1.append(list1)
        ans2=int(fp.readline())
	l2=[]
        list2=fp.readline().split()
	list2=map(int,list2)
	l2.append(list2)
        list2=fp.readline().split()
	list2=map(int,list2)
	l2.append(list2)
        list2=fp.readline().split()
	list2=map(int,list2)
	l2.append(list2)
        list2=fp.readline().split()
	list2=map(int,list2)
	l2.append(list2)
	count=0
	for j in range(4):
		if l1[ans1-1][j] in l2[ans2-1]:
			num= l1[ans1-1][j]
			count+=1
	if count==1:
                ptr.write("Case #{}: {}\n".format(i+1,num))   
	elif count>1 and count <=4:
		 ptr.write("Case #{}: {}\n".format(i+1,"Bad magician!"))  
	elif count==0:
		ptr.write("Case #{}: {}\n".format(i+1,"Volunteer cheated!"))   
	else:
		pass
