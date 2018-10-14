# coding: utf8

import os, sys, re, string

def solve(row):
	ss = row.split(' ')
	C = int(ss[0])
	if C == 0:
		merge = {}
	else:
		m = ss[1]
		merge = {(m[0], m[1]): [m[2]], (m[1], m[0]): [m[2]]}
	D = int(ss[1 + C])
	if D == 0:
		dele = {}
	else:
		d = ss[1 + C + 1]
		dele = {(d[0], d[1]): 1, (d[1], d[0]): 1}
	lists = map(lambda x: x, ss[-1])	
	index = 1
	while index < len(lists):
		target = lists[index]
		mkey = (lists[index - 1], target)
		if merge.has_key(mkey):
			lists = lists[:index - 1] + merge[mkey] + lists[index+1:]
			continue
		del_flag = False
		for i in xrange(index - 1, -1, -1):
			dkey = (lists[i], target)
			if dele.has_key(dkey):
				lists = lists[index+1:]
				del_flag = True
				index = 1
				break
		if not del_flag:
			index += 1
	return '[' + ', '.join(lists) + ']'

def main():
	T = int(sys.stdin.readline())
	for i in xrange(T):
		print 'Case #%d: %s' % (i + 1, solve(sys.stdin.readline().strip()))

if __name__ == '__main__':
	main()


