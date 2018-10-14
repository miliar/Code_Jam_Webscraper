def solve(T):
	magic1 = int(raw_input())
	num1 = []
	for i in range(4):
		num1.append([int(x) for x in raw_input().split(' ')])
	magic2 = int(raw_input())
	num2 = []
	for i in range(4):
		num2.append([int(x) for x in raw_input().split(' ')])

	ret = [x for x in num1[magic1 - 1] if x in num2[magic2 - 1]]
	if len(ret) > 1:
		pr = 'Bad magician!'
	elif len(ret) is 0:
		pr = 'Volunteer cheated!'
	else:
		pr = ret[0]

	print 'Case #{T}: {pr}'.format(T=T+1, pr=pr)

if __name__ == '__main__':
	T = int(raw_input())
	for i in range(T):
		solve(i)