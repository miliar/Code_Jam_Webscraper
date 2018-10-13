import sys

sys.stdin = open('B-large.in', 'r')
sys.stdout = open('B-large.out', 'w')

for t in range(int(input())):
	a = list(map(int, input()))
	k = -1
	for i in range(1, len(a)):
		if a[i-1] > a[i]:
			k = i
			break

	if k != -1:
		for i in range(k, -1, -1):
			if i == 0 or a[i-1] < a[i]:
				a[i] -= 1
				for j in range(i+1, len(a)):
					a[j] = 9
				break

	print('Case #%d: ' % (t+1), end = '')
	print(int(''.join(map(str, a))))