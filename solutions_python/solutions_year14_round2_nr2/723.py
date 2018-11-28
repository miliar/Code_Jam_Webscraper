ptr=open("B-small-attempt0.in","r")
fp=open("output.txt","w")

num_cases=int(ptr.readline())

for i in range(num_cases):
	data=ptr.readline().split()
	data=map(int,data)
	num1,num2,limit=data
	count = 0
	for j in range(num1):
		for k in range(num2):
			if j & k < limit:
				count+=1

	fp.write("Case #{}: {}\n".format(i+1,count))
