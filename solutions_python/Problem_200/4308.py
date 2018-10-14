# Tidy Numbers
# suhas kashyap
# kashyap 07
# kashyapsuhas07@gmail.com

def foo(num):
	n = 0
	for m in range(0, len(num)):
		n = n * 10 + int(num[m]) - 48
	return n


if __name__ == '__main__':
	T = input()	# T test cases
	for i in range(0, len(T)):
		flag = 0

		num = input()

		if len(num) == 1:
			print('Case #', i+1, ': ', num, sep='')
			continue
		for j in range(1, len(num)):
			if num[i] < num[i-1]:
				flag = 1
				break
		if flag == 0:
			print('Case #', i+1, ': ', foo(num), sep='')
		else:
			for k in range(0, len(num) -1):
				if num[i] >= num[i+1]:
					num[i] = num[i] - 1
					for l in range(0, len(num)):
						num[i+1] == '9'
						break
			print('Case #', i+1, ': ', foo(num), sep='')