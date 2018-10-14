import sys
import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import random


def main():
	sys.stdin = open('main.in', 'r')
	sys.stdout = open('main.out', 'w')

	n = int(input())
	count = 1

	while count <= n:
		r1 = int(input())
		l1 = []
		for x in range(4):
			l1.append(list(map(int, input().split())))

		r2 = int(input())
		l2 = []
		for y in range(4):
			l2.append(list(map(int, input().split())))

		s = set(l1[r1-1]) & set(l2[r2-1])

		if len(s) == 1:
			print('Case #' + str(count) + ': ' + str(s.pop()))

		elif len(s) > 1:
			print('Case #' + str(count) + ': Bad magician!')

		else:
			print('Case #' + str(count) + ': Volunteer cheated!')

		count = count+1

	sys.stdin.close()
	sys.stdout.close()

if __name__ == '__main__':
	main()
