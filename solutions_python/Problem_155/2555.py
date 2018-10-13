#!/usr/bin/env python3.4

def nextTest(num):
	stuff = input().split()
	s_max = int(stuff[0])
	total = 0
	to_add = 0
	for i in range(s_max+1):
		if total < i:
			to_add += i - total
			total += i - total
		total += int(stuff[1][i])
	print('Case #%d: %d' % (num, to_add))

def main():
	tests = int(input())
	for i in range(tests):
		nextTest(i+1)

if __name__ == '__main__':
	main()
