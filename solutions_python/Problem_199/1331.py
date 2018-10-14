#!/usr/local/bin/python3
import sys

def find_ans(s,k):
	res = 0
	s = list(s)
	for cur in range(len(s)):
		if s[cur] == '-':
			if cur + k > len(s):
				return -1
			res += 1
			for j in range(cur, cur + k):
				if s[j] == '-':
					s[j] = '+'
				else:
					s[j] = '-'
	return res

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s,k = input().split()
        k = int(k)
        res = find_ans(s,k)
        if res != -1:
            print ('Case #{}: {}'.format(i + 1, res))
        else:
        	print ('Case #{}: IMPOSSIBLE'.format(i + 1))
