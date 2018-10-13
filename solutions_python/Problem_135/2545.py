f=open('A-small-attempt1.in','r')
f1=open('output.in','w')
case=0;
for inp in f:
	break;
#input is the no. of inputs
input=int(inp)
for i in range(input):
	j=0
	while True:
		if(j==0):
			r1=f.readline()
			r_no1=int(r1)
			for k in range(r_no1):
				row1=f.readline()
			print(row1)
			for k in range(4-r_no1):
				r2=f.readline()
			r2=f.readline()
		j=5
		if(j==5):
			r_no2=int(r2)
			for k in range(r_no2):
				row2=f.readline()
			print(row2)
			for k in range(4-r_no2):
				f.readline()
			j=9
			#row1, row2 are the two required rows
			flag=0;
			for m in row1.split():
				for n in row2.split():
					if(m==n):
						ans=m;
						flag+=1
			case+=1
			if(flag==1):
				f1.write("Case #"+str(case)+": "+str(ans)+"\n")
				print("Case #"+str(case)+": "+str(ans))
			elif(flag==0):
				f1.write("Case #"+str(case)+": Volunteer cheated!\n")
				print("Case #"+str(case)+": Volunteer cheated!")
			else:
				f1.write("Case #"+str(case)+": Bad magician!\n")
				print("case #"+str(case)+": Bad magician!")
			break;
f.close()
f1.close()