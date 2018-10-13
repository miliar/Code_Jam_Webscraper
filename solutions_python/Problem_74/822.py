# How to run:
# Get python 2.6 or later from python.org
# Put the input file in the same directory as this file
# Run pythton A_bots.py
# Output is in the output txt file


def calc(case):	

	buttons = case.split()[1:]
	sequence = [(buttons[i], int(buttons[i+1])) for i in range(0, len(buttons), 2)]

	o_time = 0
	o_pos = 1
	b_time = 0
	b_pos = 1

	for button in sequence:
		if button[0] == 'O':
			o_time = o_time + abs(o_pos - button[1]) + 1
			if o_time <= b_time:
				o_time = b_time + 1
			o_pos = button[1]

		elif button[0] == 'B':
			b_time = b_time + abs(b_pos - button[1]) + 1
			if b_time <= o_time:
				b_time = o_time + 1
			b_pos = button[1]

	
	return max(o_time, b_time)
	
		
		

f = open('A-large.in', 'r')
lines = f.readlines()   
f.close()
c = lines[0].split()[0]
#print c     
cases = [r.strip() for r in lines[1:]]
#print cases  
                       
of = open('output_a_large.txt', 'w')

for idx, case in enumerate(cases):
	of.write('Case #%(idx)i: %(i)i\n' % {'idx': idx + 1, 'i': calc(case)})                          
   
of.close()
