def matrixMultiplication(a,b):
	sign = 1
	if((a*b)<0):
		sign =-1
	if(a!=-1):
		a=abs(a)
	if(b!=-1):
		b=abs(b)
	if((a==2) & (b==3)):
		return (4*sign)
	if((a==2) & (b==4)):
		return (-3*sign)
	if((a==3) & (b==2)):
		return (-4*sign)
	if((a==3) & (b==4)):
		return (2*sign)
	if((a==4) & (b==2)):
		return (3*sign)
	if((a==4) & (b==3)):
		return (-2*sign)
	if((a==b)):
		return (-1*sign)
	if(a==(-1)):
		return (-1*b)
	if(b==(-1)):
		return (-1*a)
	if(a==1):
		return b
	if(b==1):
		return a
def checkRepeat(x):
	if((len(x)*x[0])==x):
		return True
	else:
		return False
matrix_hash = {1:1,'i':2,'j':3,'k':4,'-i':-2,'-j':-3,'-k':-4}
file_write=open("dijkstra_output.txt","w+")
#file_read=open("dijkstra_input.txt","r")
file_read=open("C-small-attempt1.in","r")
noOfTestCases=int(file_read.readline())
for i in range(1,noOfTestCases+1):
	length_of_string,repeats = (file_read.readline()).split()
	repeats=int(repeats)
	flag=0
	input_string=file_read.readline()[:-1:]
	required_string=input_string*repeats
	length_of_string=int(length_of_string)
	hashed_string=list(x for x in required_string)
	hashed_string=list(matrix_hash[x] for x in hashed_string)
	if((len(required_string)<3)|(checkRepeat(required_string))):
		file_write.write("Case #%d: %s\n"%(i,"No"))
		continue
	if((hashed_string[0]==2)&(hashed_string[1]==3)&(hashed_string[2]==4)&(len(hashed_string)==3)):
		file_write.write("Case #%d: %s\n"%(i,"Yes"))
		continue
	else:
		while(((hashed_string[0]!=2)|(hashed_string[1]!=3)|(hashed_string[2]!=4))|(flag==0)):
			if(len(hashed_string)==3):
				file_write.write("Case #%d: %s\n"%(i,"No"))
				flag=1
				break
			else:
				if(len(hashed_string)<3):
					file_write.write("Case #%d: %s\n"%(i,"No"))
					break
				while(hashed_string[0]!=2):
					first_char = hashed_string[0]
					second_char = hashed_string[1]
					product = matrixMultiplication(first_char,second_char)
					hashed_string=hashed_string[1::]
					hashed_string[0]=product
					if(hashed_string[0]==2):
						break
					if(len(hashed_string)<=3):
						flag=1
						break
				if(len(hashed_string)<3):
					file_write.write("Case #%d: %s\n"%(i,"No"))
					break
				while(hashed_string[1]!=3):
					first_char = hashed_string[1]
					second_char = hashed_string[2]
					product = matrixMultiplication(first_char,second_char)
					hashed_string=[hashed_string[0]]+hashed_string[2::]
					hashed_string[1]=product
					if(hashed_string[1]==3):
						break
					if(len(hashed_string)<=3):
						flag=1
						break
				if(len(hashed_string)<3):
					file_write.write("Case #%d: %s\n"%(i,"No"))
					break
				while(len(hashed_string)>3):
					first_char = hashed_string[2]
					second_char = hashed_string[3]
					product = matrixMultiplication(first_char,second_char)
					hashed_string=[hashed_string[0]]+[hashed_string[1]]+hashed_string[3::]
					hashed_string[2]=product
					if((hashed_string[2]==4)&(len(hashed_string)==3)):
						break
					if(len(hashed_string)<=3):
						flag=1
						break
				#print(i,hashed_string)
				if(len(hashed_string)==3):
					if((hashed_string[0]==2)&(hashed_string[1]==3)&(hashed_string[2]==4)):
						file_write.write("Case #%d: %s\n"%(i,"Yes"))
						break