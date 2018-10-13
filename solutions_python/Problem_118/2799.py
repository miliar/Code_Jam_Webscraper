from sys import stdin
import math

data = stdin.readlines()
number = int(data[0])
final = data[1:]

def is_fair(x):
	if x >= 1 and x < 10:
		return True
	elif str(x) == str(x)[::-1]:
		return True
	else:
		return False

def is_square(x):
    root = math.sqrt(x)
    if int(root) ** 2 == x: 
        return True
    else:
        return False

def check_both(start, finish):
	counter = 0
	a = int(start)
	b = int(finish)
	for i in range(a, b+1):
		if is_square(i) and is_fair(i):
			a = int(math.sqrt(i))
			if is_fair(a):
				counter = counter + 1
	return counter

open('out.txt', 'w').close()
linecount = 0	
for line in final:
	mline = line.split()
	result = check_both(mline[0], mline[1])
	output = open("out.txt", "a")
	output.write('Case #' + str(linecount+1) + ': ' + str(result) + '\n')
	linecount = linecount + 1
	output.close()
	

