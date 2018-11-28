#!/usr/bin/python
import sys

#solve case function
def solve_case(B_order_list, O_order_list, case_number):
	time = 0
	current_key = 1
	B_pos = 1
	O_pos = 1
	while 1:
		#turn init.
		if len(B_order_list) > 0:
			B_order = B_order_list[0]
		else:
			B_order = (0, 0)
		if len(O_order_list) > 0:
			O_order = O_order_list[0]
		else:
			O_order = (0, 0)
	
		#check exit condition
		if B_order[0] == 0 and O_order[0] == 0:
			print "Case #" + str(case_number) + ": " + str(time)
			break;
	
		#time count
		time = time + 1

		#Bot B move
		if B_order[0] > 0:
			if B_pos > B_order[1]:
				B_pos = B_pos - 1
			elif B_pos < B_order[1]:
				B_pos = B_pos + 1
			elif B_order[0] < O_order[0] or O_order[0] == 0:
				del B_order_list[0]
	
		#Bot O move
		if O_order[0] > 0:
			if O_pos > O_order[1]:
				O_pos = O_pos - 1
			elif O_pos < O_order[1]:
				O_pos = O_pos + 1
			elif O_order[0] < B_order[0] or B_order[0] == 0:
				del O_order_list[0]

#main
r = sys.stdin

if len(sys.argv) > 1:
	r = open(sys.argv[1], 'r')

total_cases = r.readline()
for case_number in range(1, int(total_cases) + 1):
	order_string = r.readline().strip()
	order_list = order_string.split(' ')
	B_order_list = [] 
	O_order_list = [] 
	BO_flag = 'B'
	for order_number in range(1, int(order_list[0]) + 1):
		order_bot = order_list[(order_number * 2) - 1]
		order_button = order_list[order_number * 2]
		if order_bot == 'B':
			B_order_list.append((order_number,int(order_button)))
		else:
			O_order_list.append((order_number,int(order_button)))
	solve_case(B_order_list, O_order_list, case_number)

