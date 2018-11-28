# probA.py
import re
import sys

input_data = sys.stdin.readlines()
num_cases = int(input_data[0])

for x in range(num_cases):
	i = 1 + (x * 5)
	o_wins = False
	x_wins = False
	full = True


	# check for wins horizontally
	for row in range(4):
		if re.match("[OT]{4}", input_data[i+row]):
			o_wins = True
		if re.match("[XT]{4}", input_data[i+row]):
			x_wins = True
		# also check for full
		if re.search("\.", input_data[i+row]):
			full = False

	# check for wins vertically
	for col in range(4):
		vert = input_data[i][col] + input_data[i+1][col] + input_data[i+2][col] + input_data[i+3][col]
		if re.match("[OT]{4}", vert):
			o_wins = True
		if re.match("[XT]{4}", vert):
			x_wins = True

	# check diags
	diag1 = input_data[i][0] + input_data[i+1][1] + input_data[i+2][2] + input_data[i+3][3]
	diag2 = input_data[i][3] + input_data[i+1][2] + input_data[i+2][1] + input_data[i+3][0]
	if re.match("[OT]{4}", diag1) or re.match("[OT]{4}", diag2):
		o_wins = True
	if re.match("[XT]{4}", diag1) or re.match("[XT]{4}", diag2):
		x_wins = True

	if (x_wins and o_wins) or (not x_wins and not o_wins and full):
		print "Case #%d: Draw" % (x+1)
	elif x_wins:
		print "Case #%d: X won" % (x+1)
	elif o_wins:
		print "Case #%d: O won" % (x+1)
	else:
		print "Case #%d: Game has not completed" % (x+1)