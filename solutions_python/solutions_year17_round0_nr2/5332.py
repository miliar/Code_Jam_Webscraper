

#a= input("Input File name: ")
f=open('/home/sony/Desktop/codejam/B-small-attempt.in','r')
p=open('output4.out','w')
count=0
for j in f.readlines():
	if count==0:
		count+=1
		continue
	for i in range(int(j),0,-1):
		if ((i%10)>=((i//10)%10)>=((i//100)%10)>=((i//1000)%10)) or i ==1:
			b=i
			p.writelines("Case #"+str(count)+": "+str(b)+"\n")
			count+=1
			break


	
p.close()
print("output file created")

