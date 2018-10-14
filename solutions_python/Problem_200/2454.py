def tidy(a):
	if(a == sorted(a)):
		return True
	else:
		return False
		
file1 = open("large")
file2 = open("large-3.out",'w+')
m = 1
file1.readline()
for line in file1:
	numList = list(str(line))
	j = len(numList) - 2
	while(tidy(numList[:len(numList)-1]) is not True):
		numList[j] = 9
		numList[j] = str(numList[j])
		if(j > 0):
			numList[j-1] = int(numList[j-1]) - 1
			numList[j-1] = str(numList[j-1])
		elif(j == 0):
			numList[j] = int(numList[j]) - 1
			numList[j] = str(numList[j])
		j-=1
	Ans = int("".join(numList))
	file2.writelines("Case #{0}: {1}\n".format(m,Ans))
	m+=1
file2.close()
		
		