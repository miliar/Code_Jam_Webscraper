#!/usr/bin/python
from math import ceil


fin = open('C-small-attempt0.in')
fout = open('c.out', 'w')
num = int(fin.readline())
l=1


def check(a):
	c = str(a)
	b = list(c)
	b.reverse()
	return ''.join(b) == c

def getn(start, end):
	ans = []
	while not start > end:
		if check(start):
			if check(start*start):
				ans.append(start)
		start += 1
	return len(ans)

while l <= num:
	start, end = fin.readline().split('\n')[0].split(' ')
	start = int(start)
	end = int(end)
	pre = 'Case #'+str(l)+': '
	fout.write(pre + str(getn(int(ceil(start**0.5)), int(end**0.5))) + '\n')
	l += 1