## Determines the smallest number of flips required to flip str into a string of "+" using a flipper of size k, output IMPOSSIBLE otherwise
def flip(str, k):
	str = list(str)
	n = len(str)
	count = 0
	for i in range(n-k+1):
		if str[i] == "-":
			for j in range(i,i+k):
				## Flip the substring of size k starting from entry i
				if str[j] == "+":
					str[j] = "-"
				else:
					str[j] = "+"
			count = count + 1

	## Check if the last k entries are all "+"
	for i in range(n-k,n):
		if str[i] == "-":
			count = "IMPOSSIBLE"

	return count


print flip("---+-++-",3)
print flip("+++++",4)
print flip("-+-+-",4)



## I/O Handler
fIn = open('A_1.txt', 'r')
fOut = open('A_1_sol.txt','w+')
nCases = int(fIn.readline())
for i in range(nCases):
	t = fIn.readline()
	str, k = t.split(" ")
	k = int(k)
	ans = flip(str,k)
	output = "Case #{}: {}\n".format(i+1,ans)
	fOut.write(output)
fIn.close
fOut.close


