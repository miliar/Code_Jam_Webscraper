## Determines the largest tidy number in [1,n]
def tidy(num):
	d = len(str(num))
	for i in range(d):
		candList = map(int, str(num)) # Initialize candidate solution
		for j in range(i+1,d):
			candList[j] = candList[i]
		cand = int(''.join(map(str,candList))) 
		if cand > num: 
			candList[i] = candList[i] - 1
			for j in range(i+1,d):
				candList[j] = 9
			if candList[0] == 0: # Check if first digit is zero
				cand = int(''.join(map(str,candList[1:])))
			else:
				cand = int(''.join(map(str,candList)))
			break
	return cand


print tidy(132)
print tidy(1000)
print tidy(7)
print tidy(111111111111111110)



## I/O Handler
fIn = open('B_1.txt', 'r')
fOut = open('B_1_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
	num = int(t)
	ans = tidy(num)
	output = "Case #{}: {}\n".format(i+1,ans)
	fOut.write(output)
fIn.close
fOut.close


