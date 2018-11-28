#!/usr/bin/env python

# base elements : Q, W, E, R, A, S, D, F
base_elements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
combines = {}
opposed = {}
for e in base_elements:
	combines[e] = {}
	opposed[e] = [] 


input_file = open('input.txt', 'r')
cases_num = input_file.readline()

cases_num = int(cases_num)
case_strings = []

for index, line in enumerate(input_file.readlines()):
	case_strings.append(line)

#print case_strings

def solveInvocation(combines, opposed, invocation_len, invocation):
	#print '============================================================'
	#print 'invocation: ' + invocation
	curr = ''
	for i in range(invocation_len):
		char = invocation[i]
		#print 'ulazi znak: ' + char
		if len(curr) == 0:
			curr = char
			continue
		if combines.has_key(curr[-1]) and combines[curr[-1]].has_key(char):
			curr = curr[:-1] + combines[curr[-1]][char]
			#print 'kombiniram, curr: ' + curr
		else:
			if opposed[char]:
				for x in opposed[char]:
					if curr.find(x) > -1:
						curr = ''
						#print 'ponistava se'
						break
				if len(curr) != 0:
					curr += char
					#print 'ne kombiniran, curr: ' + curr
			else:
				curr += char
				#print 'ne kombiniram, curr: ' + curr

	return list(curr) 

for cs_i, cs in enumerate(case_strings):
	cs = cs.strip()
	#print cs
	combines_num, cs = cs.split(' ', 1)
	combines_num = int(combines_num)
	for i in range(combines_num):
		com, cs = cs.split(' ', 1)
		#print com
		combines[com[0]][com[1]] = com[2]
		combines[com[1]][com[0]] = com[2]
	#print str(combines)

	opposed_num, cs = cs.split(' ', 1)
	opposed_num = int(opposed_num)
	for i in range(opposed_num):
		opp, cs = cs.split(' ', 1)
		#print 'opppppppppppppppppp: ' + opp 
		opposed[opp[0]].append(opp[1])
		opposed[opp[1]].append(opp[0])

	#print str(opposed)

	invocation_num, cs = cs.split(' ', 1)
	invocation_num = int(invocation_num)

	print 'Case #' + str(cs_i +1) + ': ' + str(solveInvocation(combines, opposed, invocation_num, cs))
	
	for e in base_elements:
		combines[e] = {}
		opposed[e] = []


	

	
		
