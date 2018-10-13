T=int(raw_input())
def f1_sub(str1,str2):
	r=0
	if str1==str2: return 0
	else:
		i,j=0,0
		while i <> len(str1) and j<> len(str2) :
			if str1[i]==str2[j]:
				i,j=i+1,j+1
			elif str1[i]==str1[i-1]: 
				i,r=i+1,r+1
			elif str2[j]==str2[j-1]: 
				j,r=j+1,r+1
			else: return -1
		if i==len(str1):
			while j <> len(str2):
				if str2[j] ==str2[j-1]: 
					j,r=j+1,r+1
				else: return -1
		if j==len(str2):
			while i <> len(str1):
				if str1[i] ==str1[i]: 
					i=i+1
					r=r+1
				else: return -1
		return r
for t in range(1,T+1):
	N=int(raw_input())
	str1=[]
	for i in range(N):
		str1.append(raw_input())
	str1.sort(key=lambda x: len(x))
	num=f1_sub(str1[0],str1[1])
	print "Case #%d:"%(t),num if num >=0 else "Fegla Won" 

	

