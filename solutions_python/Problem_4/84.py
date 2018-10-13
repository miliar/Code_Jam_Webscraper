Input = open("A-large.in")
Output = open("A-large.out","w")

N = int(Input.readline()[:-1])

for i in range(N):
	
	V1 = []
	V2 = []
	Min = 0
	n = int(Input.readline()[:-1])
	L = Input.readline()[:-1].split(" ")
	for j in range(n):
		V1.append(int(L[j]))
	L = Input.readline()[:-1].split(" ")
	for j in range(n):
		V2.append(int(L[j]))
	V1.sort()
	V2.sort()
	V2.reverse()
	for j in range(n):
		Min += V1[j]*V2[j]
	Write = "Case #"+str(i+1)+": "+str(Min)+"\n"
	Output.writelines(Write)
	print Write
	
Input.close()
Output.close()
