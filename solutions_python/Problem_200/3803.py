import os,string
content=[]
output=[]
with open("B-large.in") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
case_num=0
for N in content :
	case_num+=1
	a=N
	b=len(a)
	#i=0
	#j=0
	#print b
	s=a
	f=0
	for t in range(b) :
		f=0
		for i in range(int(b)-1):
			#print "+1" , a
			if int(a[i])>int(a[i+1]):
				s=a[0:i]
				#print "+2"
				s+=str(int(a[i])-1)
				for j in range(i,int(b)-1):
					s+="9"
					#print "+3",s
			elif (i==int(b)-2) :
				f=f+1
				break
	        #	f=1
	        #	break
		a=s
		if f>=2 :
			break
	#	if f==1 :
	#		break


	            #print s
	#print int(s)
	output.append("Case #" + str(case_num) + ": " + str(int(s)))

fo = open("tidy_2.in","wb")
for j in output :
	print j
	fo.write(j+"\n")
fo.close()
