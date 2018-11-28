from math import sqrt

def checkPalineDrome(x):
	if len(x) == 1:
		return True
	else:
		for i in range(0,int(len(x)/2)):
			if x[i] != x[len(x)-i-1]:
				return False
		return True

f = open('input.txt','r')
w = open('output.txt', 'w')

testcase = int(f.readline())

for a in range (0, testcase):
	AB = f.readline().split(' ')
	A = int(AB[0])
	B = int(AB[1])
	count = 0
	for i in range (A,B+1):
		if checkPalineDrome(str(i)):
			sqrt_i = sqrt(i)
			if sqrt_i%1 == 0:
				if checkPalineDrome(str(int(sqrt_i))):
					count += 1

	msg = 'Case #{0}: {1}'.format(a+1,str(count))
	print(msg)
	w.write(msg)
	if a != testcase-1:
		w.write("\n")