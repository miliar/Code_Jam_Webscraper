import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

cnt_tests = int(input())

for test in range(cnt_tests):
	d, n = list(map(int, input().split()))
	l = []
	rez = int(1e23)
	for j in range(n):
		pos, speed = map(int, input().split())
		rez = min(rez, d / ((d - pos) / speed))
	print('Case #%d:' % (test + 1), rez)

