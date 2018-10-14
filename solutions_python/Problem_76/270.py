#!/usr/bin/env python
fout = open('c.out', 'w')

def max(a, b):
	if a > b:
		return a
	return b

def solve(test, a):
	global fout
	n = len(a)
	s1 = [0 for i in range(n)]
	s2 = [0 for i in range(n)]
	s3 = [0 for i in range(n)]
	s4 = [0 for i in range(n)]
	s1[0] = a[0]
	s3[0] = a[0]
	for i in range(1, n):
		s1[i] = s1[i - 1] ^ a[i]
		s3[i] = s3[i - 1] + a[i]

	if s1[n - 1] != 0:
		fout.write("Case #" + str(test + 1) + ": NO\n")
		return
	s2[n - 1] = a[n - 1]
	s4[n - 1] = a[n - 1]
	i = n - 2
	while i >= 0:
		s2[i] = s2[i + 1] ^ a[i]
		s4[i] = s4[i + 1] + a[i]
		i -= 1
	sol = 0
	for i in range(n - 1):
		if s1[i] == s2[i + 1]:
			sol = max(sol, max(s3[i], s4[i + 1]))

	fout.write('Case #' + str(test+1) + ': ' + str(sol) +'\n')

def main():
	file = open('c.in', 'r')
	T = int(file.readline())
	for test in range(T):
		n = int(file.readline())
		a = [int(i) for i in file.readline().split()]
		a.sort()
		solve(test, a)
		
if __name__ == "__main__":
	main()
