#coding: utf-8
#!/usr/bin/env python2.7
import sys
import copy

def main():
	line = []
	for l in sys.stdin: line.append(l)

	counter = 0
	num = int(line[counter][:-1])
	counter += 1

	for i in range(1, num+1):
		block_num = int(line[counter][:-1])
		counter += 1
		naomi_block_list = map(float, line[counter][:-1].split())
		counter += 1
		ken_block_list = map(float, line[counter][:-1].split())
		counter += 1

		both_block_list = []
		for naomi_block in naomi_block_list:
			both_block_list.append((naomi_block, 0))
		for ken_block in ken_block_list:
			both_block_list.append((ken_block, 1))
		both_block_list.sort()
	
		stack1 = 0
		stack2 = 0
		point1 = 0
		point2 = 0
		for block, flag in both_block_list:
			if flag == 1:
				stack1 += 1
				if stack2 > 0: 
					stack2 -= 1
					point2 += 1
			if flag == 0:
				stack2 += 1
				if stack1 > 0: 
					stack1 -= 1
					point1 += 1


		print 'Case #%s: %d %d' % (str(i), point1, block_num-point2)

if __name__ == '__main__':
	main()
