# Google Code Jam 2011 - Qualification Round
# Javier Fernandez (javierfdr@gmail.com)

import collections

base_elements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
base_set = set(base_elements)


def magicka(actions_list,comb_hash,result_hash, opposition_hash):
	magic_list = collections.deque()
	for a in actions_list:
		
		if (len(magic_list)==0):
			magic_list = collections.deque([a])
			continue
		# check if are combinable	
		if are_bases(a,magic_list[-1]):
			# check if combines the action with the last added
			comb = combines(a,magic_list[-1],comb_hash,result_hash)
			if comb[0]:
				magic_list.pop()
				magic_list.append(comb[1])
				continue		
		
		# check opposition
		did_break= False
		for e in magic_list:
			# check if there is a current opposition
			if are_in_opposition(a,e,opposition_hash):
				magic_list = collections.deque()
				did_break = True
				break
		if did_break:
			magic_list = collections.deque()
		else:
			magic_list.append(a)
	
	return list(magic_list)
		
def combines(e1,e2,comb_hash,result_hash):
	if (e1 in comb_hash[e2]) or (e2 in comb_hash[e1]):
		return (True,result_hash[e1+e2])
	return (False,'')

def are_bases(e1,e2):
	if e1 in base_set and e2 in base_set:
		return True
	else:
		return False

def make_combination_hashes(comb_list):
	#initialize
	c_hash = {}
	comb_hash = {}
	for be in base_elements:
		comb_hash[be]=set()
	
	#add oppositions to lists	
	for comb in comb_list:
		comb_hash[comb[0]].add(comb[1])
		comb_hash[comb[1]].add(comb[0])
		
		c_hash[comb[0]+comb[1]] = comb[2]
		c_hash[comb[1]+comb[0]] = comb[2]
		
	return (comb_hash,c_hash)	
		
				
def make_opposition_hash(op_list):
	#initialize
	op_hash = {}
	for be in base_elements:
		op_hash[be]=set()
	
	#add oppositions to lists	
	for op in op_list:
		op_hash[op[0]].add(op[1])
		op_hash[op[1]].add(op[0])
	return op_hash

def are_in_opposition(op_element,a,o_hash):
	if not are_bases(op_element,a):
		return False
	
	if a in o_hash[op_element]:
		return True
	return False

def parse_file(in_file,out_file):
	num_cases= int(in_file.readline())
	for c in range(num_cases):
		comb_list =[]
		op_list=[]
		actions = ''
		case_data = in_file.readline().split()
		
		index = 0
		num_combs = int(case_data[index])
		index+=1
		for n in range(num_combs):
			comb_list.append(case_data[index])
			index+=1
		num_ops = int(case_data[index])
		index+=1
		
		for n in range(num_ops):
			op_list.append(case_data[index])
			index+=1
		index+=1
		actions = case_data[index]
		
		(comb_hash,result_hash) = make_combination_hashes(comb_list)
		opposition_hash = make_opposition_hash(op_list)

		print '-----------------------'
		print 'Case +'+str(c+1)
		print comb_list
		print op_list
		print '\n'

		m_result = magicka(actions,comb_hash,result_hash,opposition_hash)
		res_string ='[' +  ', '.join(m_result)+']'
	
		out_file.write('Case #'+str(c+1)+': '+res_string+"\n")

import sys
in_file = sys.stdin
out_file = open('output.out','w+')
parse_file(in_file,out_file)

