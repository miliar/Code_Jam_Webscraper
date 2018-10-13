file = open("newfile.txt", "w")
file1 = open("D-large.in.txt","r")
data = file1.readlines()
T=int(data[0])
for tu in range (1,T+1):
	k=(tu*3)-2
	data1=data[k].split()
	n=int(data1[0])
	data1=data[k+1].split()
	naomi=[]
	ken=[]
	for i in data1:
		naomi.append(float(i))
	data1=data[k+2].split()
	for i in data1:
		ken.append(float(i))
	ken.sort()
	naomi.sort()
	s1=0
	s2=0
	zu=0
	for i in range(n):
		if naomi[i]>ken[zu]:
			s1+=1
			zu+=1
	for i in range(n):
		flag=0
		for j in range(n):
			if ken[j]>naomi[-(i+1)]:
				flag=1
				ken[j]=0.0
				break
		if flag==0:
			s2+=1
			for ken1 in ken:
				if ken1!=0.0:
					ken1=0.0
					break
			

	file.write("Case #%d: %d %d\n"% (tu,s1,s2))
	
	
file1.close()
file.close()
