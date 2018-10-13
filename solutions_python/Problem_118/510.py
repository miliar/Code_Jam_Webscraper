#!/usr/bin python
# coding: utf-8

from math import sqrt

def palindrome(n):
	return [int(str(i) + str(i)[-1-(n % 2)::-1]) for i in range(10**((n + 1) / 2-1), 10**((n + 1) / 2))]

def generate(A, B):
	a, b = int(sqrt(A)), int(sqrt(B))
	l = []
	for n in xrange(len(str(a)), len(str(b)) + 1):
		l += [i for i in palindrome(n) if i * i >= A and i * i <= B and str(i * i) == str(i * i)[::-1]]
	return l

def main():
	fin = file('C-large-1.in', 'r')
	fout = file('C-large-1.out', 'w')

	T = int(fin.readline().split()[0])
	for t in xrange(1, T + 1):
		ant = 0
		A, B = [int(n) for n in fin.readline().split()]
		fout.write('Case #' + str(t) + ': ' + str(len(generate(A, B))) + '\n')
		# print t

if __name__ == '__main__':
	main()