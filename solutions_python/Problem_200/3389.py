def findTidyNumber(listN):
	for i in range(0,len(listN)):
		if i+1 < len(listN):
			if listN[i] > listN[i+1]:
				listN[i] = listN[i] - 1
				for j in range(i+1,len(listN)):
					listN[j] = 9
				findTidyNumber(listN)
		else:
			return listN

t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
	n = int(input())
	num = list(str(n))
	listN = [int(x) for x in str(n)]
	listN = findTidyNumber(listN)
	for i in range(0,len(listN)):
		if listN[0] == 0:
			listN.pop(0)
			break;
	numeber = ''.join(str(x) for x in listN)
	print("Case #{}: {}".format(j,numeber))

