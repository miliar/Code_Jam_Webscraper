def flipit():
	test= int(input())
	strings=[]
	maxflip=[]
	kk=[]
	for i in range(test):
		kk.append(input())
		x=kk[i].split(" ")
		strings.append(x[0])
		maxflip.append(int(str(x[1])))
	result=[]
	for i in range(test):
		count=0
		if strings[i].count("+")==len(strings[i]):
			result.append(0)
			continue
		flip=int(maxflip[i])
		if len(strings[i])<flip:
			result.append("IMPOSSIBLE")
			continue
		for j in range(len(strings[i])-flip+1):
			if strings[i][j]=="-":
				strings[i]=strings[i][:j]+ ''.join('-' if x == '+' else '+' for x in strings[i][j:j+flip]) + strings[i][j+flip:]
				count+=1
		if strings[i].count("-")>0:
			result.append("IMPOSSIBLE")
			continue
		result.append(int(count))
	for i in range(1,len(result)+1):
		print("Case","#"+str(i)+":", result[i-1])
flipit()
