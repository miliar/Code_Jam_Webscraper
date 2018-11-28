# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer

def findBefore(strOfN):
	lenOfStrN = len(strOfN)
	if lenOfStrN<2:
		return strOfN
	if strOfN[0]=="9":
		for countI in range(1,lenOfStrN):
			if strOfN[countI]<"9":
				return "8"+"9"*(lenOfStrN-1)

		return strOfN
	if strOfN[0] <strOfN[1]:
		return  strOfN[0] + findBefore(strOfN[1:])


	countI = 1
	for i in range(1,lenOfStrN):

		if strOfN[0]==strOfN[countI]:
			countI = countI +1
			continue
		elif strOfN[0]<strOfN[countI]:
			return  strOfN[0:countI] + findBefore(strOfN[countI:])
		else :
			if strOfN[0]=="1":
				return "9"*(lenOfStrN-1)
			else :
				return str(int(strOfN[0])-1)+"9"*(lenOfStrN-1)

	return str(strOfN)





for i in range(1, t + 1):
	n = [int(s) for s in input().split(" ")]  
	numberOfN = n[0]
	return_n = findBefore(str(numberOfN))
	print("Case #{}: {}".format(i, return_n))
	#print("Case #{}: ".format(i)+return_n)
  