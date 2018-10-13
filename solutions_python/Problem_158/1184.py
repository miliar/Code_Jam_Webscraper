f=open("D-small-attempt8.in","r")
f2=open("output2.out", "w")
data=f.read().splitlines()
p=int(data[0])
l=1
result=""
for i in range(p):
	#print i+1
	temp=data[l].split(" ")
	#print temp
	l+=1
	x=int(temp[0])
	r=int(temp[1])
	p=int(temp[2])
	#check 1
	if r*p % x==0:
		if x==1 or x==2:
			if r*p >= x:
				result+="Case #"+str(i+1)+": "+"GABRIEL"+"\n"
				#print "GABRIEL"
			else:
				result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
				#print "RICHARD"
		else:
			if r*p > x:
				if min(r,p) > float(x/2):
					result+="Case #"+str(i+1)+": "+"GABRIEL"+"\n"
					#print "GABRIEL"
				else:
					result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
					#print "RICHARD"
			else:
				result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
				#print "RICHARD"
	else:
		result+="Case #"+str(i+1)+": "+"RICHARD"+"\n"
		#print "RICHARD"
#print result
f2.write(result)
f2.close()
