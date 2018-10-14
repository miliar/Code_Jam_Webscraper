import os,string,math
def rs(S,i) :
	j = 1
	while  True :
		if S[i+j] == '1' :
			break 
		#print "+1"
		j+=1
		
	return j-1

def ls(S,i) :
	j=1
	while True :
		if S[i-j] == '1' :
			break
		j+=1
	return j-1


content=[]
output=[]
with open("C-small-2-attempt1.in") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
for NK in content :
	nk=NK.split()
	N=int(nk[0])
	k=int(nk[1])
	s=[]
	#s_1=""
	s.append("1")
	#s_1+="1"
	for i in range(N) :
		s.append("0")
		#s_1+= " 0"
	s.append("1")
	#s_1+=" 1"

	#s=s_1.split()
	#print s
	#for i in range(k,0,-1) :
		#print i
	j = int(math.log(k,2)) + 1
	#print j
	P=""
	n=N
	occ=[]
	num=k
	for i in range(j) :
	#	print "+1"
		if N==k :
			output.append([0,0])
			break

		if i == 0 :
	#		print "+2"
			num=num-1
			if n%2 == 0:
	#			print "+4"
				s[int(n/2)] = "1"
				occ.append(int(n/2))
				P+="1"
			else :
	#			print "+5"
				s[int((n+1)/2)] = "1"
				occ.append((n+1)/2)
				P+="0"
		else :
			LR=[]
			for abc in range(int(math.pow(2,i-1))) :
				LR.append(0)

	#		print "+3"
			for a in range(int(math.pow(2,i))) :
	#			print "a"
				num=num-1
			#	LR=[]
			#	for abc in range(int(math.pow(2,i-1))) :
			#		LR.append(0)
				y=int(math.pow(2,i-1))
				x= int(y + a%y - 1)
	#			print "y,x=",y,x
				if P[x] == "0" and LR[int(a%y)]==0:
					
					LR[a%y]=1
					n1=ls(s,occ[x])
					n2=occ[x]-n1-1
	#				print "b",n1,n2,LR
					if n1%2 ==0 :
						s[n2+(n1/2)] ="1"
						occ.append(n2+(n1/2))
						P+="1"
					else :
						s[n2+(n1+1)/2] ="1"
						occ.append(n2+(n1+1)/2)
						P+="0"
				elif P[x] == "1" and LR[int(a%y)]==0 :
	#				print "c"
					LR[a%y]=1
					n1=rs(s,occ[x])
					if n1%2==0 :
						s[occ[x]+n1/2]="1"
						occ.append(occ[x]+n1/2)
						P+="1"
					else :
						s[occ[x]+(n1+1)/2]="1"
						occ.append(occ[x]+(n1+1)/2)
						P+="0"
				elif P[x] == "1" and LR[int(a%y)]==1:
	#				print "d"
					LR[a%y]=1
					n1=ls(s,occ[x])
					n2=occ[x]-n1-1
					if n1%2 ==0 :
						s[n2+(n1/2)] ="1"
						occ.append(n2+(n1/2))
						P+="1"
					else :
						s[n2+(n1+1)/2] ="1"
						occ.append(n2+(n1+1)/2)
						P+="0"
				elif P[x] == "0" and LR[int(a%y)]==1 :
					
					LR[a%y]=1
					n1=rs(s,occ[x])
	#				print "e",n1
					if n1%2==0 :
						s[occ[x]+n1/2]="1"
						occ.append(occ[x]+n1/2)
						P+="1"
					else :
						s[occ[x]+(n1+1)/2]="1"
						occ.append(occ[x]+(n1+1)/2)
						P+="0"
				if num==0 :
				#	ans1=[]
				#	ans1.append(max(ls(s,occ[-1]),rs(s,occ[-1])))
				#	ans1.append(min(ls(s,occ[-1]),rs(s,occ[-1])))
				#	output.append(ans1)
					break
		if num==0 :
			ans1=[]
			ans1.append(max(ls(s,occ[-1]),rs(s,occ[-1])))
			ans1.append(min(ls(s,occ[-1]),rs(s,occ[-1])))
			output.append(ans1)
			break

	#print s
#print output
num0=1
fo = open("BS_ans_small2_1.in","wb")
for j in output :
	j_1= "Case #" + str(num0) + ": " + str(j[0]) + " " + str(j[1])  
	print j_1
	fo.write(j_1+"\n")
	num0+=1
fo.close()
#	print nk
#print content