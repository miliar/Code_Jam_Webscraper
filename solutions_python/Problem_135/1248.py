import os
import string
from string import split


#ip = open("input.txt", 'r')

n =  int(raw_input())

for case in range(0,n):

	nr1 = int(raw_input())
	l1 = [int(i) for i in raw_input().split()]
	l2 = [int(i) for i in raw_input().split()]
	l3 = [int(i) for i in raw_input().split()]
	l4 = [int(i) for i in raw_input().split()]

	if nr1 == 1:
		x = l1
	elif nr1 == 2:
		x = l2
	elif nr1 == 3:
		x = l3
	elif nr1 == 4:
		x = l4

	nr2 = int(raw_input())
	l1_2 = [int(i) for i in raw_input().split()]
	l2_2 = [int(i) for i in raw_input().split()]
	l3_2 = [int(i) for i in raw_input().split()]
	l4_2 = [int(i) for i in raw_input().split()]

	if nr2 == 1:
		y = l1_2
	elif nr2 == 2:
		y = l2_2
	elif nr2 == 3:
		y = l3_2
	elif nr2 == 4:
		y = l4_2



#	print x
#	print y

	op = list(set(x) & set(y))
	#op = [itm for itm in x if itm in y]
	if len(op) > 1:
		secondPart = "Bad magician!"
	elif len(op) == 0:
		secondPart = "Volunteer cheated!"
	else:
		secondPart = int(op[0])

	print "Case #" + str(case+1) + ": " + str(secondPart)

