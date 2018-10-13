
f=open("A-small-attempt1.in","r")

T=int(f.readline().strip())
answers=[]

for i in range(T):
	N=int(f.readline().strip())
	strings=[f.readline().strip() for j in range(N)]
	rivers=[]
	counts=[]
	for k in range(N):
		rivers.append([])
		counts.append([])
		for p in range(len(strings[k])):
			if len(rivers[k])==0 or rivers[k][-1]!=strings[k][p]:
				rivers[k].append(strings[k][p])
				counts[k].append(0)
			counts[k][-1]+=1
	
	bo=1
	for k in range(N-1):
		if len(rivers[k])!=len(rivers[k+1]):
			bo=0
			answers.append("Fegla Won")
			break
		else:
			bo=1
			for l in range(len(rivers[k])):
				if rivers[k][l]!=rivers[k+1][l]:
					answers.append("Fegla Won")
					bo=0
					break
			if not bo:
				break
				
	if bo:
		lettercounts=[[] for j in range(len(rivers[0]))]
		for river in range(len(rivers)):
			for l in range(len(rivers[0])):
				lettercounts[l].append(counts[river][l])
		print(lettercounts)
		minimizer=[1000 for j in range(len(rivers[0]))]
		for j in range(1,101):
			for letter in range(len(lettercounts)):
				sum=0
				for number in lettercounts[letter]:
					sum+=abs(j-number)
				minimizer[letter]=min(minimizer[letter],sum)
		totalsum=0
		for num in minimizer:
			totalsum+=num
		answers.append(totalsum)
	
	
		
				

f.close()
f=open("OUTPUT.txt","w")
for i in range(T):
	f.write("Case #{}: {}\n".format(i+1,answers[i]))
f.close()
