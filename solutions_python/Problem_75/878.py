#!/usr/bin/python

f = open('B-large.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('magicka_large_result.txt', 'w')
comb_elm = {}
opp_elm = {}

def print_dict(in_dict):
	for formula, result in in_dict.items():
		print "    ",formula," => ",result

def check_opposites(inp):
	for formula, result in opp_elm.items():
		formula_fr = formula[0]
		formula_bk = formula[1]
		if (formula_fr in inp) and (formula_bk in inp):
			return True
	return False

for i in range (0,numcase):
	comb_elm = {}
	opp_elm = {}
	line = f.readline()
	linelist = line.split()
	num_comb = int(linelist[0])
	for j in range (0,num_comb):
		new_formula = linelist[j+1]
		newbase = new_formula[0:2]
		newresult = new_formula[2]
		comb_elm[newbase] = newresult
	#print "  Combinations:"
	#print_dict(comb_elm)

	offset = num_comb+1
	num_opp = int(linelist[offset])
	offset = offset + 1
	for j in range (0,num_opp):
		new_formula = linelist[offset+j]
		newbase = new_formula
		opp_elm[newbase] = ""
	#print "  Opposites:"
	#print_dict(opp_elm)

	offset = offset + num_opp
	inv_len = int(linelist[offset])
	inv = linelist[offset+1]
	#Start
	x = 0
	temp_out = []
	for j in range (0,inv_len):
		x = len(temp_out)
		if x == 0:
			temp_out.append(inv[j])
			#x = x +1
		else:
			cur_comb = temp_out[x-1] + inv[j]
			rev_comb = inv[j] + temp_out[x-1]
			if cur_comb in comb_elm:
				temp_out.pop()
				temp_out.append(comb_elm[cur_comb])
			elif rev_comb in comb_elm:
				temp_out.pop()
				temp_out.append(comb_elm[rev_comb])
			else:
				temp_out.append(inv[j])
			if len(temp_out) > 1:
				if check_opposites(temp_out):
					temp_out = []
	
	final_elm = "["
	for j in range(0,len(temp_out)):
		if j == 0:
			final_elm = final_elm + temp_out[j]
		else:
			final_elm = final_elm + ", " + temp_out[j]
		
	final_elm = final_elm + "]"
	answer = "Case #"+str(i+1)+": "+ final_elm	
	#print answer
	fout.write(answer)
	fout.write('\n')



f.close()
fout.close()
