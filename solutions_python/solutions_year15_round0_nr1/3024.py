#!/usr/bin/python

global people_standing
people_standing=0

def standing_ovate(no_people):
	global people_standing
	
	if no_people == 0:
		return people_standing
	
	people_standing += no_people
	return people_standing

def get_people_required(max_shyness, shyness_indices):
	global people_standing
	people_required=0
	people_standing=0
	#print "shyness_indices : %s" % shyness_indices
	for shy_idx in range(max_shyness + 1):
		#print shyness_indices[shy_idx], shy_idx, people_standing
		if shy_idx <= people_standing:
			#print "standing_ovate - %s" % shyness_indices[shy_idx]
			standing_ovate(shyness_indices[shy_idx])
		else:
			if shyness_indices[shy_idx] > 0:
				introduced_people=shy_idx - people_standing
				people_required += introduced_people 
				standing_ovate(introduced_people) 
				standing_ovate(shyness_indices[shy_idx])
			
	return people_required

no_of_cases=raw_input()
no_of_cases=int(no_of_cases)
while no_of_cases > 0:
	curr_case=1
	while curr_case <= no_of_cases:
		case_str=raw_input()
		case_str_comp=case_str.split()
		max_shyness=int(case_str_comp[0])
		shyness_indices=[int(idx) for idx in case_str_comp[1]]
		people_required = get_people_required(max_shyness, shyness_indices)

		
		print "Case #%d: %d\n" % (curr_case, people_required)
		#print "#%s"%curr_case, max_shyness, [(i, shyness_indices[i]) for i in range(len(shyness_indices))], people_required
		curr_case += 1
		no_of_cases -= 1
