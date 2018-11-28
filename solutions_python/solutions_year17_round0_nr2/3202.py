t = int(input())  # read a line with a single integer

a = "abcdef"

def calcul(n) : 
	
	for i in range(0,len(n) - 1) :
		if (n[i] > n[i+1]) : 
			return calcul(str(int(n[:i+1])-1)) + "9"*(len(n)-i-1)
	return n;


for i in range(1, t + 1):
	n = input()
	n = calcul(n)
	n = int(n)
	print("Case #{}: {}".format(i, n))
	