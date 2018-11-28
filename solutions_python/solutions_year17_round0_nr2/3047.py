
#x is a string
def findNear(x):
	if(int(x) < 10): return x
	else:
		x1 = int(x[0])
		x2 = findNear(x[1::])
		xx2 = int(x2[0])

		if (x1 > xx2):
			x1 = x1-1;
			res = ""
			for i in range(len(x2)):
				res += "9"
			return str(x1) + res

		return str(x1) + x2



file = open("input2.txt")
L = file.read().splitlines()

k = L[0]
for x in range(1,int(k)+1):
	ans = int(findNear(str(L[x])))
	print ("Case #{}: {}".format(x, ans if ans != -1 else "IMPOSSIBLE"))
