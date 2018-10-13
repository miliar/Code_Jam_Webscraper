f = open('C-small-attempt0.in')
line = f.readline()

count=int(line)
for wd in range(1,count+1):
	line=f.readline();
	s=line.split();
	r=int(s[0]);
	k=int(s[1]);
	N=int(s[2])
	sum=0;
	i=0;
	j=-1;
	temp=0;
	total=0
	line=f.readline();
	s=line.split();
	for i in range(1,r+1):
		sum=0;
		j=(j+1)%N;
		i=j;
		
		while(True):
			sum=sum+int(s[j])
			if(sum>k):
							
				sum=sum-int(s[j])
				j=(j-1)%N;
				break;
			elif(sum==k):
				
				break;
			else:
				
				j=(j+1)%N;
				if(i==j):
					break;
				continue;
	

		total=total+sum	

		
	print "Case #"+str(wd)+": "+str(total)


f.close()
