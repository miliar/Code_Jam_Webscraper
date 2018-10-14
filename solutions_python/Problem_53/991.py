# a snapper is a device with two modes: on and off
# a snapper toggles to the other mode when fingers are clicked.  it must have power to switch modes.
#

#now to parse

input = []
with open("A-small-attempt0.in") as f:
	for line in f:
		input.append(line)

case_count = 1

output = open('output.out', 'w')

for case in input[1:]:
	chain_size = int(case.split()[0])
	number_of_clicks = int(case.split()[1])


	snapper_chain = []
	for x in range(chain_size):
		snapper_chain.append(bool())
		
	print snapper_chain


	for click in range(number_of_clicks):
		for snapper in range(chain_size):
			#if it's on, turn it off, but go on to the next one and toggle
			if (snapper_chain[snapper]):
				snapper_chain[snapper] = False
			else:
				snapper_chain[snapper] = True
				break
				
	print snapper_chain
				
	is_on = True
				
	for snapper in snapper_chain:
		if (snapper):
			pass
		else:
			is_on = False
			break
		
		
	if (is_on):
		print 'It\'s on!'
		output.write('Case #{0}: ON\n'.format(case_count))
	else:
		print 'It\'s off!'
		output.write('Case #{0}: OFF\n'.format(case_count))
	
	case_count += 1
	
