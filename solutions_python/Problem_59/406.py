#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def f(n):
	'''テストサンプル

	>>> f(1)
	2
	>>> f(2)
	3
	'''
	return n+1

def count_need_mkdir(exist_paths,create_paths):
	'''必要なmkdirを数える

	>>> count_need_mkdir([],['/home/gcj/finals', '/home/gcj/quals'])
	4

	>>> count_need_mkdir(['/chicken', '/chicken/egg'],['/chicken'])
	0

	>>> count_need_mkdir(['/a'],['/a/b', '/a/c', '/b/b'])
	4
	'''
	count = 0
	for path in create_paths:
		dirs = path.strip('/').split('/')
		sub_path = ''
		for dir in dirs:
			sub_path += '/'+dir
			if not sub_path in exist_paths:
				count += 1
				exist_paths.append(sub_path)
#				print 'add: '+sub_path

	return count

def main():
	test_case_count = int(sys.stdin.readline())
	for test_case_number in xrange(1,test_case_count+1):
		(exist_path_count,create_path_count) = sys.stdin.readline().split()
		exist_paths = []
		for j in xrange(0,int(exist_path_count)):
			exist_paths.append(sys.stdin.readline().strip())
		create_paths = []
		for j in xrange(0,int(create_path_count)):
			create_paths.append(sys.stdin.readline().strip())

		need_mkdir = count_need_mkdir(exist_paths,create_paths)
		print 'Case #'+str(test_case_number)+': '+str(need_mkdir)

def test():
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	main()

