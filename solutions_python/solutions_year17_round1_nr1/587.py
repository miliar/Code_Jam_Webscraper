n=int(input())

for i in range(n) :
	a,b=[int(e) for e in input().split()]
	l=[]
	for _ in range(a) :
		l.append(input())
	for ligne in range(a) :
		for col in range(b) :
			if l[ligne][col]!="?" :
				left=l[ligne][col]
				#print("left:",left)
			if l[ligne][col]=="?" :
				#l[ligne][col]=left
				l[ligne]=l[ligne][:col]+left+l[ligne][col+1:]
				#print(" inter :",l)
		boo=l[ligne]!="?"*b
		while "?" in l[ligne] and boo :
			ind=0
			#print("ETAT l :",l)
			#print(" LIGNE :",l[ligne])
			#print("ind :",ind)
			#print("l[ligne][ind] : ",l[ligne][ind])
			while l[ligne][ind]=="?" :
				ind=ind+1
			#print("l[ligne]",l[ligne])
			#print("i: ",ind)
			right=l[ligne][ind]
			l[ligne]=l[ligne][:ind].replace("?",right)+l[ligne][ind:]
		left="?"
	while "?"*b in l :
		#print("? ga aru")
		ind=l.index("?"*b)
		if ind!=0 :
			bf = l[ind-1]
			#print(bf)
			l[ind]=bf
		else :
			irf=1
			while l[irf]=="?"*b :
				irf=irf+1
			l[ind]=l[irf]
	print("Case #"+str(i+1)+":")
	for el in range(a) :
		print(l[el])

