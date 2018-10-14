from math import ceil

def minTime(n, a):
	minT = 10 ** 100
	for i in range(1, max(a) + 1):
		t = 0
		for j in range(n):
			if a[j] >= i:
				t += (ceil(a[j]/i) - 1)
		minT = min(minT, t + i)
	return minT


def main():
	t = int(input())
	for k in range(1, t + 1):
		D = int(input())
		p = list(map(int, input().split()))
		print('Case #'+str(k) + ':', minTime(D, p))

if __name__ == '__main__':
	main()