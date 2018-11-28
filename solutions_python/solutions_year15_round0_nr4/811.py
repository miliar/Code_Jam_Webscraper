input_file = "D-small-attempt2.in"
#input_file = "input_d.txt"
output_file = "output_d.txt"

data = open(input_file, 'r')
output = open(output_file, 'w')

testcase = (int)(data.readline())
for i in range(testcase):
	row = data.readline().split()
	x = (int)(row[0])
	r = (int)(row[1])
	c = (int)(row[2])
	winner = ""
	#set to be r > c 
	if c > r:
		temp = c
		c = r
		r = temp

	if (( r*c % x) == 0):
		for j in range(1, (int)((x+1)/2)):
				if (x/2 >= c):
					winner = "RICHARD"
		if not(winner):
			winner = "GABRIEL"
	else:
		winner = "RICHARD"

	#print("winner is %s" % winner)	
	output.write("Case #%d: %s\n" %(i+1, winner))

output.close()