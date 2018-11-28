import math
def isPalindrome(s):
	t = str(s)
	return t == t[::-1]

fin = open('input.txt','r')
fout = open('output.txt','w')
t = int(fin.readline())
for i in range(1,t+1):
	a, b = [int(x) for x in fin.readline().split()]
	x = int(math.ceil(math.sqrt(a)));
	y = int(math.floor(math.sqrt(b)));
	count = 0
	j = x
	while j < (y+1):
		if (isPalindrome(j) and isPalindrome(j*j)):
			count += 1
		j = j+1
	fout.write("Case #" + str(i) + ": " + str(count) + "\n")
fin.close()
fout.close()