#!/usr/bin/env python

pancakeDict = {'-': '1', '+': '0'}

def PancakeFlipper(line):
	ret = 0
	pancake, flipper = line.split()
	pancake_num, pancake_mask = len(pancake), int(''.join(map(pancakeDict.get, pancake)), 2)
	flipper_num, flipper_mask = int(flipper), (1 << int(flipper)) - 1

	for i in xrange(pancake_num - flipper_num + 1):
		if pancake_mask & (1 << i):
			ret += 1
			pancake_mask ^= (flipper_mask << i)
	return 'IMPOSSIBLE' if pancake_mask else str(ret)

fileOut = open('file.out.txt', 'w')

with open('file.in.txt', 'r') as fileIn:
	for i in xrange(int(fileIn.readline())):
		fileOut.write('Case #{}: {}\n'.format(i + 1, PancakeFlipper(fileIn.readline().strip())))

fileIn.close()
fileOut.close()
