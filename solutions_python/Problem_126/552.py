#!/usr/bin/env python
#-*- coding: utf-8 -*-

VOWELS = set(['a', 'e', 'i', 'o', 'u'])


def differenceLen(s):
	l = 0
	for x in s:
		if not x in VOWELS:
			l += 1
	return l


def findAllWellSubstringInALen(s, a):
	gset = set()
	for x in xrange(a, len(s) + 1):
		
		if differenceLen(s[x-a:x]) == a:
			gset.add((x-a, s[x-a:x]))
			
			for j in xrange(x, len(s) + 1):
				for i in xrange(x-a + 1):
		
					gset.add((i, s[i:j]))
	ans = len(gset)
	
	return ans




def solve(text, n):
	return findAllWellSubstringInALen(text, n)



def main():
	fout = open('output.txt', 'w')
	ans = []
	with open('input.txt', 'r') as fin:
		t = int(fin.readline())
		for line in xrange(t):
			text, n = fin.readline().split(' ')
			ans.append("Case #{0}: {1}".format(line + 1, solve(text, int(n))))

	fout.write("\n".join(ans))
	fout.close()


if __name__ == '__main__':
	main()
