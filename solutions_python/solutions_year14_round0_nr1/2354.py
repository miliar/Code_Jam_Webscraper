import math

n = int(raw_input())
for iterator in range(n):
	first_select_row = int(raw_input())
	first_choose = []
	for i in range(4):
		if i == first_select_row-1:
			first_choose = map(int,raw_input().strip().split(' '))
		else:
			temp = raw_input()
	second_select_row = int(raw_input())
	second_choose = []
	for i in range(4):
		if i == second_select_row-1:
			second_choose = map(int,raw_input().strip().split(' '))
		else:
			temp = raw_input()
	#print first_choose,second_choose
	intersect = [i for i in first_choose if i in second_choose]
	if len(intersect) == 1:
		print "Case #%d: %d" % (iterator+1, intersect[0])
	elif len(intersect) == 0:
		print "Case #%d: Volunteer cheated!" % (iterator+1)
	else:
		print "Case #%d: Bad magician!" % (iterator+1)
		
