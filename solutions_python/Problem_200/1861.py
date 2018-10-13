def isTidy(num):
	for i in range(len(num) - 1):
		if num[i] > num[i + 1]:
			return False
	return True
def gen9(num):
	s = ''
	for i in range(num):
		s += '9'
	return s
for t in range(int(input())):
	n = input()
	l = len(n)
	i = 1
	f = n
	while True:
		if isTidy(f):
			print('Case #{}: {}'.format(t + 1,int(f)))
			break
		f = str(int(n[:l - i]) - 1) + gen9(i)
		i += 1