#!/usr/bin/env python
#coding=utf8
		
def toint(x):
	if x=="i":
		return 2
	elif x=="j":
		return 3
	elif x=="k":
		return 4
	print "*******"

def multiply(x, y):
	if x<0:
		sig = -1
		x = -x
	else:
		sig = 1
	if x==1:
		return y*sig
	elif y==1:
		return x*sig
	elif x==y:
		return -1*sig
	elif x==2 and y==3:
		return 4*sig
	elif x==2 and y==4:
		return -3*sig
	elif x==3 and y==2:
		return -4*sig
	elif x==3 and y==4:
		return 2*sig
	elif x==4 and y==2:
		return 3*sig
	elif x==4 and y==3:
		return -2*sig

# source = open("/Users/chalk/Downloads/tmp")
source = open("/Users/chalk/Downloads/C-small-attempt3.in")
tests = int(source.readline())
res = []
for test in range(0, tests):
	line1 = source.readline().strip()
	L = int(line1.split()[0])
	X = int(line1.split()[1])
	line2 = source.readline().strip()
	string = line2*X

	if len(string)<3:
		res.append("NO")
		continue
	current = 1
	pos = 2
	for char in string:
		current = multiply(current, toint(char))
		if current == pos and pos<=3:
			current = 1
			pos += 1

	if pos==4 and current == 4:
		res.append("YES")
	else:
		res.append("NO")
	
for i in range(0, tests):	 
	print "Case #" + str(i+1) + ": " + str(res[i])

