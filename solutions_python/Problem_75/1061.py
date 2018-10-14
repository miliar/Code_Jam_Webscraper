import os, sys
lines = open(sys.argv[1]).read().split('\n')[1:]
def apply_rules(rules, input, i):
	for rule in rules:
		A = ''.join(sorted(rule[0:2])) 
		B = ''.join(sorted([input[i], input[i-1] ]))
		if A==B:
			#print 'input was',input,'found transform',rule
			input = input[:i-1] + rule[2] + input[i+1:]
			return input
	return input

def apply_opposed(rules, input, i):
	for rule in rules:
		#print 'checking for opposing in',input[:i+1]
		if rule[0] in input[:i+1] and rule[1] in input[:i+1]:
			input = input[i+1:]
		'''
		if rule[0] == input[i] and rule[1] == input[i+1]:
			print 'input was',input,'found opposing',rule
			input = input[i+2:]
			return input
		'''
	return input

for c in range(len(lines)):
	tokens = lines[c].split(' ')
	if len(tokens) == 1: continue
	n_trans = int(tokens[0])
	transforms = tokens[1:1+n_trans]
	n_opposed = int(tokens[1+n_trans])
	opposed = tokens[2+n_trans:2+n_trans+n_opposed]
	input = tokens[-1]

	while True:
		old_length = len(input)
		old_input = input

		for i in range(1,len(input)):
			input = apply_rules(transforms, input, i)
			if input != old_input: break
			input = apply_opposed(opposed, input, i)
			if input != old_input: break

		if len(input) == old_length: break
	output = ''
	for ch in input:
		output += ch + ', '
	print 'Case #%d: [%s]'%(c+1, output[:-2])


