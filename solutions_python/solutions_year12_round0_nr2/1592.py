def give_scores(total):
	ret = {}
	avg = int(total/3)
	remainder = total - avg*3
	if remainder == 0:
		ret['non-sig'] = avg
		if avg-1 >= 0 and avg+1 <= 10:
			ret['sig'] = avg+1
	elif remainder == 1:
		if avg+1 <= 10:
			ret['non-sig'] = avg+1
		if avg+1 <= 10 and avg-1 >=0:
			ret['sig'] = avg+1
	else:
		if avg+1 <= 10:
			ret['non-sig'] = avg+1
		if avg+2 <= 10:
			ret['sig'] = avg+2
	return ret


num_to_scores = {}
best_to_sig = {}
for best in range(11):
	best_to_sig[best] = {}

for total in range(31):
	bests = give_scores(total)
	if bests.has_key('sig') and bests.has_key('non-sig'):
		if bests['sig'] == bests['non-sig']:
			for num in range(bests['sig']+1):
				best_to_sig[num][total] = 'both'
		elif bests['sig'] > bests['non-sig']:
			for num in range(bests['sig']):
				best_to_sig[num][total] = 'both'
			best_to_sig[bests['sig']][total] = 'sig'
		else:
			for num in range(bests['non-sig']):
				best_to_sig[num][total] = 'both'
			best_to_sig[bests['non-sig']][total] = 'non-sig'
	elif bests.has_key('sig'):
		for num in range(bests['sig']+1):
			best_to_sig[num][total] = 'sig'
	else:
		for num in range(bests['non-sig']+1):
			best_to_sig[num][total] = 'non-sig'

def get_max(sup_list, num_suprising, num_not_suprising):
	sig, non_sig, both, neither = sup_list
	max = both
	max += min(num_suprising, sig)
	max += min(num_not_suprising, non_sig)
	return max
	
def get_sup(best, totals):
	sig  = 0
	non_sig = 0
	both = 0
	neither = 0
	for total in totals:
		if not best_to_sig[best].has_key(total):
			neither +=1 
		elif best_to_sig[best][total] == 'both':
			both +=1
		elif best_to_sig[best][total] == 'sig':
			sig +=1
		else:			
			non_sig +=1
	return [sig, non_sig, both, neither]
	
reader = open('large2.in', 'r')
writer = open('large2.out', 'w')
num_lines = int(reader.readline())
for input_number in range(1, num_lines+1):
	line = reader.readline()
	input_vals = [int(num) for num in line.split(' ')]
	num_googlers = input_vals[0]
	num_suprising = input_vals[1]
	num_non_suprising = num_googlers - num_suprising
	best = input_vals[2]
	totals = input_vals[3:]
	sup_list = get_sup(best, totals)
	max_val = get_max(sup_list, num_suprising, num_non_suprising)
	writer.write('Case #'+str(input_number)+": "+str(max_val)+'\n')
	


# translation_dict = {'a':'y', 'o':'e', 'z':'q', 'q':'z'}
# 
# examples = {'ejp mysljylc kd kxveddknmc re jsicpdrysi':'our language is impossible to understand', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':'there are twenty six factorial possibilities','de kr kd eoya kw aej tysr re ujdr lkgc jv':'so it is okay if you want to just give up'}
# 
# for key,val in examples.items():
# 		for char_idx in range(len(key)):
# 			translation_dict[key[char_idx]] = val[char_idx]
# 
# def translate_to_english(text):
# 	output_arr = [];
# 	for char_idx in range(len(text)-1):
# 		output_arr.append(translation_dict[text[char_idx]])
# 	return ''.join(output_arr)
# 
# reader = open('small1.in', 'r')
# writer = open('small1.out', 'w')
# num_lines = int(reader.readline())
# for input_number in range(1, num_lines+1):
# 	line = reader.readline()
# 	writer.write('Case #'+str(input_number)+": "+translate_to_english(line)+'\n')