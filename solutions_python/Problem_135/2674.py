'''python template for google code jam
'''

import math
import sys

# sys.stdin = open('1.in', 'r')
# sys.stdout = open('1.out', 'w')

sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdout = open('A-small-attempt0.out', 'w')

# sys.stdin = open('X-large.in', 'r')
# sys.stdout = open('X-large.out', 'w')

# input
# a, b = map(int, sys.stdin.readline().split())

def SameSet(a, b):
	ans = list(set(a) & set(b))
	return ans

t = int(sys.stdin.readline())
for cc in range(1, t+1):
	ans = [[], []]
	for j in range(2):
		r = int(sys.stdin.readline())
		numbers = []
		for i in range(4):
			numbers.append(map(int, sys.stdin.readline().split()))
		ans[j] = numbers[r-1]
	answer = SameSet(ans[0], ans[1])
	if len(answer) == 0:
		answer = 'Volunteer cheated!'
	elif len(answer) == 1:
		answer = answer[0]
	else:
		answer = 'Bad magician!'
	sys.stdout.write('Case #' + str(cc) + ': ' + str(answer) + '\n')
  
