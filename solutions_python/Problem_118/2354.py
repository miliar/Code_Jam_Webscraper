import math

fi = open("input.txt", "r")
fo = open("output.txt", "w")

t = int(fi.readline())

def isp(arg):
	arg = str(arg)
	for i in range(len(arg) // 2):
		if arg[i] != arg[len(arg) - i - 1]:
			return False
	return True
	
for i in range(t):
	a, b = [int(x) for x in fi.readline().split()]
	ans = 0;
	l  = math.floor(math.sqrt(a))
	r  =  math.floor(math.sqrt(b)) + 2
	print(l, r)
	for j in range(l, r):
		if j * j < a:
			continue
		if j * j > b:
			break;
		print(j, isp(j), isp(j *j))
		if isp(j) and isp(j * j):
			ans = ans + 1;
	fo.write("Case #" + str(i + 1) + ": " + str(ans) + "\n")

fo.close()	
