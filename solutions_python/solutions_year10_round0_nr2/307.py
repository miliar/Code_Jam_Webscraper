r = open('c:\B-large.in', 'r')
w = open('c:\B-large.out', 'w')

s = r.readline()
C = int(s)
for i in range(1, C+1):
	s = r.readline().split(' ')
	N = int(s[0])
	X = int(s[1])
	H = 0
	print(N)
	for j in range(2, N+1):
		Y = int(s[j]) - X
		
		if Y < 0:
			Y = - Y
		if H == 0:
			H = Y
		else:
			while Y % H != 0:
				b = Y % H
				Y = H
				H = b
	ans = X % H
	if ans != 0:
		ans = H - ans
	w.write('Case #'+str(i)+': ' + str(ans) + '\n')
print(10 ** 50)
