from sys import stdin
from collections import Counter

def get():
	row = int(input())
	[stdin.readline() for i in xrange(row - 1)]
	line = stdin.readline().split()
	[stdin.readline() for i in xrange(4 - row)]
	return line

for case in xrange(int(input())):
	dup =  set(get()) & set(get())
	l = len(dup)
	ans = 'Volunteer cheated!' if l == 0 else dup.pop() if l == 1 else 'Bad magician!'
	print('Case #{}: {}'.format(case + 1, ans))
