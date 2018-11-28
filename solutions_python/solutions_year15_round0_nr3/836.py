import itertools
import sys
from functools import wraps

def cache(wrapped_func):
	cache = {}
	@wraps (wrapped_func)
	def wrapper(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = wrapped_func(*args)
			return cache[args]
		except TypeError:
			return wrapped_func(*args)
	return wrapper

trans = {"11":"1","1i":"i","1j":"j","1k":"k","i1":"i","ii":"-1","ij":"k","ik":"-j","j1":"j","ji":"-k","jj":"-1","jk":"i","k1":"k","ki":"j","kj":"-i","kk":"-1"}
cache_glob = {}
@cache

def rec_mult(string_to_multiply):
	if len(string_to_multiply) == 1:
		return string_to_multiply
	if len(string_to_multiply) == 2:
		return t
	if cache_glob.has_key(string_to_multiply):
		return cache_glob[string_to_multiply]
	else:
		string_length = len(string_to_multiply)
		result = trans[rec_mult(string_to_multiply[:string_length/2]) + rec_mult(string_to_multiply[string_length/2:])]
		cache_glob[string_to_multiply] = result
		return result

def mult(string_to_multiply):
	minus = 0
	if "-" in string_to_multiply:
		minus+=1
		string_to_multiply = string_to_multiply.replace("-", "")
	
	work_string = string_to_multiply
	while len(work_string) >1:
		res = trans[work_string[:2]]
		if "-" in res:
			minus +=1
			res = res.replace("-","")
		work_string = res + work_string[2:]
	if minus %2 == 0:
		return work_string
	else:
		return "-" + work_string #we have a minus

def split_generator(text):
    letters = [i for i in text]
    ns = range(1, len(letters))
    for idxs in itertools.combinations(ns, 2):
        yield [''.join(letters[i:j]) for i, j in zip((0,) + idxs, idxs + (None,))]

# def match(to_mult,letter):
# 	if cache_glob.has_key(to_mult):
# 		return cache_glob[to_mult] == letter
# 	elif len(to_mult)>2 and cache_glob.has_key(to_mult[:-1]):
# 		result = mult(cache_glob[to_mult[:-1]] + to_mult[-1])
# 		cache_glob[to_mult] = result
# 		return result == letter
# 	else:
# 		result = mult(to_mult)
# 		cache_glob[to_mult] = result
# 		return result == letter

def match(to_mult,letter):
	if cache_glob.has_key(to_mult):
		return cache_glob[to_mult] == letter
	elif len(to_mult)>2 and cache_glob.has_key(to_mult[:-1]):
		result = mult(cache_glob[to_mult[:-1]] + to_mult[-1])
		cache_glob[to_mult] = result
		return result == letter
	else:
		result = mult(to_mult)
		cache_glob[to_mult] = result
		return result == letter

if __name__ == "__main__":
	with open(sys.argv[1],"r") as f:
		data = f.readlines()
	data = [i.replace("\n","") for i in data]
	num_of_test_cases = int(data[0])
	test_cases_results = []
	cases_data = data[1:]
	for test_i in range(num_of_test_cases):
		# print test_i
		is_possible = False
		L_X,input_string = cases_data[2*test_i:2*test_i+2]
		X_input = int(L_X.split(" ")[1])
		L_input = int(L_X.split(" ")[0])
		final_string = input_string*X_input
		string_len = L_input * X_input
		if(len(set([i for i in input_string]))) == 1:
			test_cases_results.append(is_possible)
			# print test_i,is_possible
			continue
		
		#Solution #1
		# for perm in split_generator(final_string):
		# 	if not match(perm[0], "i"):
		# 		continue
		# 	if not match(perm[1], "j"):
		# 		continue
		# 	if match(perm[2], "k"):
		# 		is_possible=True
		# 		break

		# #Solution #2
		# ind_1 = 0
		# ind_2 = 0
		# ind_3 = 0
		# while(ind_1 < string_len):
		# 	ind_2 = ind_1 +1
		# 	while(ind_2 < string_len):
		# 		ind_3 = ind_2 + 1
		# 		while(ind_3 < string_len):
		# 			print ind_1,ind_2,ind_3
		# 			if not match(final_string[:ind_1], "i"):
		# 				if ind_1 != string_len-1:
		# 					ind_1+=1
		# 				else:
		# 					break
		# 				if ind_2 == ind_1 and ind_1 != string_len-1:
		# 					ind_2+=1
		# 				if ind_3 == ind_2 and ind_2 != string_len-1:
		# 					ind_3+=1
		# 				continue
		# 			if not match(final_string[ind_2:ind_3],"j"):
		# 				if ind_2 != string_len-1:
		# 					ind_2 +=1
		# 				else:
		# 					break
		# 				if ind_2 == ind_3 and ind_2 != string_len-1:
		# 					ind_3+=1
		# 				continue
		# 			if match(final_string[ind_3:], "k"):
		# 				is_possible = True
		# 				break
		# 			else:
		# 				if ind_3 != string_len -1:
		# 					ind_3+=1
		# 			ind_3 +=1
		# 		if is_possible or string_len-1 in [ind_1,ind_2]:
		# 			break
		# 		ind_2+=1
		# 	if is_possible or ind_1 == string_len-1:
		# 		break
		# 	ind_1+=1
		
		#Solution #3
		# i_idx = []
		# k_idx = []
		# for ind_1 in range(string_len):
		# 	if match(final_string[:ind_1], "i"):
		# 		i_idx.append(ind_1)
		# if i_idx:
		# 	for i_ocr in i_idx:
		# 		for ind_2 in range(i_ocr,string_len):
		# 			if match(final_string[i_ocr:ind_2], "j"):
		# 				k_idx.append(ind_2)
		# else:
		# 	test_cases_results.append(is_possible)
		# 	print test_i,is_possible
		# 	continue			
		# if k_idx:
		# 	for k_ocr in k_idx:
		# 		for ind_3 in range(k_ocr,string_len):
		# 			if match(final_string[k_ocr:ind_3], "k"):
		# 				is_possible = True
		# 				break
		# 		if is_possible:
		# 			break

		#Solution #4
		found_i = False
		found_j = False
		for ind_1 in range(string_len):
			if found_i: break
			if match(final_string[:ind_1], "i"):
				found_i = True
				for ind_2 in range(ind_1,string_len):
					if found_j: break
					if match(final_string[ind_1:ind_2], "j"):
						found_j = True
						for ind_3 in range(ind_2,string_len):
							if match(final_string[ind_2:], "k"):
								is_possible = True
								break
					if is_possible:
						break
			if is_possible:
				break	

		test_cases_results.append(is_possible)
		# print test_i,is_possible
	for idx,res in enumerate(test_cases_results):
		print "Case #%d: %s" % (idx+1, "YES" if res else "NO")