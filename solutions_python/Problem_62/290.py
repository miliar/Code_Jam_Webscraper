input = open("A-large.in","r")
output = open("output.txt","w")

counter = int(input.readline())
for i in range(1,counter+1):
	wireNum = int(input.readline())
	if wireNum == 1:
		input.readline()
		result = 0
	elif wireNum==2:
		A = input.readline().split()
		B = input.readline().split()
		if (int(A[0])-int(B[0]))*(int(A[1])-int(B[1]))<0:
			result = 1
		else:
			result = 0
	else:
		A =[]
		for j in range(1,wireNum+1):
			A+=[input.readline().split(),]
		result = 0
		first = 0
		while first < wireNum-1:
			second = first+1
			while second<wireNum:
				if (int(A[first][0])-int(A[second][0]))*(int(A[first][1])-int(A[second][1]))<0:
					result += 1
				second+=1
			first+=1
	output.write("Case #%d: %d\n"%(i,result))
		
		
		