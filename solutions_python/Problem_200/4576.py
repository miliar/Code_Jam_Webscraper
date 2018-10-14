

with open("B-large.in",'r') as f:
	data = f.read().split('\n')

output = open("BB-large.out",'w')

numsOfInput = data[0]
for i in range(1, int(numsOfInput)+1):

	num = data[i]
	numList = [int(j) for j in list(num)]

	if len(num) == 1:
		print("Case #{}: {}".format(i, num))
		output.write("Case #{}: {}\n".format(i, num))
	else:
		for j in range(len(num)-1):
			if (numList[j] <= numList[j+1]) and (j != len(num)-2):
				continue

			elif (numList[j] <= numList[j+1]) and (j == len(num)-2):
				print("Case #{}: {}".format(i, num))
				output.write("Case #{}: {}\n".format(i, num))
				break

			else:
				k = j
				while((numList[k] <= numList[k-1]) and (k != 0)):
					k -= 1
				if numList[k] == 1:
					tidyNum = '9'*(len(num)-1)
				else:
					tidyNum = num[0:k] + str(int(num[k])-1) + '9'*(len(num)-1-k)
				print("Case #{}: {}".format(i, tidyNum))
				output.write("Case #{}: {}\n".format(i, tidyNum))
				break

output.close()





