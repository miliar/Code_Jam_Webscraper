#!/usr/bin/python
#Solution by Sajith Dilshan Edirisinghe
# email: sajithdilshan@gmail.com


ins = open( "C-small-attempt0.in", "r" )
array = []
for line in ins:
    array.append( line.split() )
array.pop(0)
i=0;
ans=[]
temp=[]
for tup in array:
	up=int(tup[1])
	low=int(tup[0])
	numlist=range(low,up+1)
	for num in numlist:
		charlist=list(str(num))
		if len(charlist)==1:
			temp=[]
		if len(charlist)==2:
			if(charlist[1]!=charlist[0]):
				x=charlist[1]+charlist[0]
				if int(x) in numlist:
					if (num,int(x)) not in temp and (int(x),num) not in temp:
						temp.append((num,int(x)))
		if len(charlist)==3:
			x=charlist[2]+charlist[0]+charlist[1]
			if int(x) in numlist and int(x)!=num:
				if (num,int(x)) not in temp and (int(x),num) not in temp:
					temp.append((num,int(x)))
			x=charlist[1]+charlist[2]+charlist[0]
			if int(x) in numlist and int(x)!=num:
				if (num,int(x)) not in temp and (int(x),num) not in temp:
					temp.append((num,int(x)))
		if len(charlist)==4:
			x=charlist[3]+charlist[0]+charlist[1]+charlist[2]
			if int(x) in numlist and int(x)!=num:
				if (num,int(x)) not in temp and (int(x),num) not in temp:
					temp.append((num,int(x)))
			x=charlist[2]+charlist[3]+charlist[0]+charlist[1]
			if int(x) in numlist and int(x)!=num:
				if (num,int(x)) not in temp and (int(x),num) not in temp:
					temp.append((num,int(x)))
			x=charlist[1]+charlist[2]+charlist[3]+charlist[0]
			if int(x) in numlist and int(x)!=num:
				if (num,int(x)) not in temp and (int(x),num) not in temp:
					temp.append((num,int(x)))
	ans.append(len(temp))
	counter=0
	temp=[]


file = open("output.txt","w")
i=0
for val in ans:
	file.write("Case #"+str(i+1)+": "+str(val)+"\n")
	i=i+1
file.close()
