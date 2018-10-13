f=open("B-small-attempt4.in","r")
f2=open("output.out", "w")
data=f.read().splitlines()
c=int(data[0])
line=1
special=0
temp=0
temp2=[]
temp3=[]
mins=0
result=""
check=True
need=False
ma=0
last=1000
for i in range(c):
	#print (i+1)
	temp=int(data[line])
	line+=1
	temp2=data[line].split(' ')
	for j in temp2:
		temp3.append(int(j))
	line+=1
	#print temp3
	ma=max(temp3)
	#print ma
	while check:

		for j in temp3:
			if j>3: need=True
		if need:
			mins+=1
			special+=1
			temp4=max(temp3)
			# temp5=temp3.index(temp4)
			# temp3.append(temp4/2)
			# temp3[temp5]=(temp4-(temp4/2))
			# need=False
			if temp4 == 9 and (5 not in temp3) and (temp3.count(9) == 1):
				#print "d5lt"
				temp5=temp3.index(temp4)
				temp3.append(3)
				temp3[temp5]=(temp4-3)
				need=False
			else:
				temp5=temp3.index(temp4)
				temp3.append(temp4/2)
				temp3[temp5]=(temp4-(temp4/2))
				need=False
			temp4=0
			temp5=0
			need=False
		else:
			mins+=1
			for k in range(len(temp3)):
				if temp3[k]>0:
					temp3[k]=(temp3[k]-1)
		
		temp6=(mins+max(temp3))
		#print temp6
		if temp6 < ma:
			if temp6<last:
				last=temp6
		#print "la: ",last, "mins: ",mins
		check=False
		for j in temp3:
			if j >0: check=True
		#print temp3
	if last < mins: mins=last
	if mins>ma: mins=ma
	need=False
	check=True
	#print "mins: ",mins
	result+="Case #"+str(i+1)+": "+str(mins)+"\n"
	#result+=str(mins)+"\n"
	mins=0
	special=0
	temp=0
	temp2=[]
	temp3=[]
	temp4=0
	temp5=0
	temp6=0
	last=1000
	ma=0
#print result
f2.write(result)
f2.close()