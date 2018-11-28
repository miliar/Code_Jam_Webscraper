from collections import defaultdict

def is_subseq_of(seq1, seq2):
	for unique_elem in set(seq1):
		if seq1.count(unique_elem) > seq2.count(unique_elem):
			return False;
	return True;

def open_all_chests(keys, unopened_chests, keys_in_chests, chests_opened_by_key, key_opening_chest, opened_chests, cached_solution, cached_fails):
	if(len(unopened_chests) == 0):
		return True
	if(len(keys) == 0):
		return False;
	keys_needed = []
	for unopened_chest in unopened_chests:
		keys_needed.append(key_opening_chest[unopened_chest])
	can_all_chests_be_opened = True
	for key in set(keys_needed):
		if(keys_needed.count(key) > keys.count(key)):
			can_all_chests_be_opened = False
			break
	if(can_all_chests_be_opened):
		opened_chests.extend(unopened_chests)
		return True

	all_keys = keys[:]
	for keys_in_chest in keys_in_chests:
		all_keys.extend(keys_in_chest)
	if is_subseq_of(keys_needed, all_keys) == False:
		return False;


	for chest in unopened_chests:
		key = key_opening_chest[chest]
		if not (key in keys):
			continue
		if(unopened_chests.count(chest) == 0):
			continue
		unopened_chests_copy = unopened_chests[:]
		keys_copy = keys[:]
		unopened_chests_copy.remove(chest)
		keys_copy.remove(key)
		keys_copy.extend(keys_in_chests[chest])
		unopened_chests_copy.sort()
		keys_copy.sort()
		
		if tuple(unopened_chests_copy) in cached_solution:
			solution_keys_needed = cached_solution[tuple(unopened_chests_copy)]
			if is_subseq_of(solution_keys_needed, keys_copy):
				opened_chests.insert(0, chest)
				return True
			else:
				continue
		if tuple(unopened_chests_copy) in cached_fails:
			cached_fail = cached_fails[tuple(unopened_chests_copy)]
			can_all_chests_be_opened = True
			for fail_key_list in cached_fail:
				if fail_key_list == keys_copy:
					can_all_chests_be_opened = False
					break;
			if can_all_chests_be_opened == False:
				continue
		can_all_chests_be_opened = open_all_chests(keys_copy, unopened_chests_copy,keys_in_chests, chests_opened_by_key, key_opening_chest,
					 opened_chests, cached_solution, cached_fails)
		if can_all_chests_be_opened:
			cached_solution[tuple(unopened_chests_copy)] = keys_copy
			opened_chests.insert(0, chest)
			return True
		cached_fails[tuple(unopened_chests_copy)].append(keys_copy)
	return False

f = open('D-small-attempt3.in', 'r')
output = open('output.txt', 'w')
tc_count = f.readline()
#print tc_count
for tc_idx in range(0, int(tc_count)):
	k, n = f.readline().strip().split()
	key_types = f.readline().strip().split()
	keys_in_chests = []
	key_opening_chest = []
	chests_opened_by_key = defaultdict(list)
	unopened_chests = []
	for chest_idx in range(0, int(n)):
		line = list(f.readline().strip().split())
		key_opening_chest.append(line[0])
		chests_opened_by_key[line[0]].append(chest_idx)
		keys_in_chests.append(line[2:])
		unopened_chests.append(chest_idx)
	opened_chests = []
	key_types.sort()
	unopened_chests.sort()
	cached_solution = {}
	cached_fails = defaultdict(list)
	can_all_chests_be_opened = open_all_chests(key_types, unopened_chests, keys_in_chests, chests_opened_by_key, key_opening_chest, opened_chests, cached_solution, cached_fails)
	result = "IMPOSSIBLE"
	if can_all_chests_be_opened:
		one_based_chest = [str(chest + 1) for chest in opened_chests]
		result = ' '.join(one_based_chest)
	#print cached_solution
	output.write("Case #" + str(tc_idx + 1) + ": " + str(result) + "\n")
