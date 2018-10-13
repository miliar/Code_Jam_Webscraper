'''
def check(x):
	for i in range(len(x)-1):
		if (x[i]) < (x[i+1]):
			return True
	return False
'''
def execute():
	n = input()
	num = int(n)

	n = n[::-1]
	for i in range(len(n)-1):
		if n[i] < n[i+1]:
			q = ''
			for j in range(i+1):
				q += '9'
			n = q + str((int(n[i+1]) + 9)%10) + n[i+2:]
			continue
	n = n[::-1].lstrip('0')
	return n	 

t = input()
t = int(t)
i = 1
while t>0:
	ans = execute()
	print("Case #" + str(i) + ": " + str(ans))
	t -= 1
	i +=1