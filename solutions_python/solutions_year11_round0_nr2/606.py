# Magicka
# Google Code Jam
# Ameer Ayoub <ameer.ayoub@gmail.com>
# 12:27pm 5/6/2011

def Magicka(combination_rules, opposition_rules, invoke_list):
	debug = False
	output_list = []
	for s in invoke_list:
		output_list.append(s)
		if debug:
			print "Processing:", s
			print output_list, "->",
		for comb_rule in combination_rules:
			if(len(output_list) > 1 and 
				((comb_rule[0] == output_list[-2:][0] 
				and comb_rule[1] == output_list[-2:][1]) or
				(comb_rule[0] == output_list[-2:][1] 
				and comb_rule[1] == output_list[-2:][0]))):
				if debug:
					print "COMBINING!", comb_rule
				output_list = output_list[0:-2]
				output_list.append(comb_rule[2])
		for rule in opposition_rules:
			if (rule[0] in output_list) and (rule[1] in output_list):
				if debug:
					print "CLEARING"
				output_list = []
		if debug:
			print output_list
	return output_list

def TestMagicka():
	print "Test Case: ", Magicka(["EEZ"], ["QE"], "QEEEERA")

def ExecuteMagicka():
	f = open("magicka.in")
	o = open("magicka.out", "w")
	num_cases = 0
	i = 0
	line = f.readline()
	if(line):
		num_cases = int(line)
	while(i < num_cases):
		line = f.readline()
		split_line = line.split(' ')
		combination_rules = []
		opposition_rules = []
		invoke_list = []
		num_comb_rules = int(split_line[0])
		j = 1
		while(j < num_comb_rules + 1):
			combination_rules.append(split_line[j])
			j += 1
		num_opposition_rules = int(split_line[j])
		j += 1
		while(j < num_comb_rules + num_opposition_rules + 2):
			opposition_rules.append(split_line[j])
			j += 1
		invoke_list_length = split_line[j]
		invoke_list = split_line[j+1]
		if(len(invoke_list) > invoke_list_length):
			# Just to ensure we conform to the specified input
			invoke_list = invoke_list[:invoke_list_length]
		result = Magicka(combination_rules, opposition_rules, invoke_list[:-1])
		output_buffer = "["
		for ch in result:
			output_buffer += str(ch)+", "
		if(len(output_buffer) > 1):
			output_buffer = output_buffer[:-2]
		output_buffer += "]"
		o.write("Case #"+str(i+1)+": "+output_buffer+"\n")
		i += 1

if __name__ == "__main__":
	#TestMagicka()
	ExecuteMagicka()