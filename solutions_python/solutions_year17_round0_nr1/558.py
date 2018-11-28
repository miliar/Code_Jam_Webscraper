# -*- coding: utf-8 -*-
# @Author: Patrice Béchard 20019173
# @Date:   2017-04-07 20:35:46
# @Last Modified time: 2017-04-07 21:00:03
#
# A. Oversized Pancake Flipper
#

def flip_pancakes(pancakes,j,sz):
	for k in range(sz):
		pancakes[j+k] = not pancakes[j+k]
	return pancakes

file = 'A-large.in'
file2 = 'output2.txt'
f = open(file)
g = open(file2,'w')
number = int(f.readline().strip())

for i in range(number):
	temp = f.readline().strip().split()
	sizeFlipper = int(temp[1])
	pancakes = []							#bool array
	nFlip = 0
	for char in temp[0]:
		if char == "+":
			pancakes.append(True)
		else:
			pancakes.append(False)
	for j in range(len(pancakes)):
		if j + sizeFlipper > len(pancakes):
			if False in pancakes:
				nFlip = "IMPOSSIBLE"
				break
		if pancakes[j] is False:
			flip_pancakes(pancakes,j,sizeFlipper)	#will now be true
			nFlip += 1
	nFlip = str(nFlip)
	out = 'Case #%d: %s\n'%(i+1,nFlip)
	g.write(out)

