#coding: utf-8
#!/usr/bin/env python2.7

import sys

def read_line():
	buf = []
	for l in sys.stdin: buf.append(l[:-1])
	return buf


def solver(list, x, y):
	all_list = []
	for i in list: 
		for j in i.split(' '):
			all_list.append(int(j))
	all_list.sort()
	all_set = set(all_list)

	int_list = []
	for i in list:
		l = []
		for j in i.split(' '):
			l.append(int(j))
		int_list.append(l)

	for num in all_set:
		for i in range(x):
			for j in range(y):
				if int_list[i][j] == num:
					if not search(int_list, i, j, x, y, num): return 0
	return 1


def search(int_list, i, j, x, y, num):
	flag = 1
	for a in range(x):
		if int_list[a][j] > num: flag = 0
	if flag: return 1
	
	flag = 1
	for b in range(y):
		if int_list[i][b] > num: flag = 0
	if flag: return 1
	else: return 0
	


def main():
	buf = read_line()
	num = int(buf[0])
	counter = 1

	for i in range(1, num+1):
		x = int(buf[counter].split(' ')[0])
		y = int(buf[counter].split(' ')[1])
		counter += 1

		list = []
		for j in range(x):
			list.append(buf[counter])
			counter += 1
		ans = solver(list, x, y)

		if ans: print 'Case #%d: YES'%(i)
		else: print 'Case #%d: NO'%(i)
		

	

if __name__ == '__main__':
	main()
