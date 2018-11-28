 
dic_num = {'0':"ZERO", '1':"ONE", '2':"TWO", '3':"THREE", '4':"FOUR", '5':"FIVE", '6':"SIX", '7':"SEVEN", '8':"EIGHT", '9':"NINE"}

full_dic = {}
	#0: {Z:# E:# R:# O:#}

if_dic_l = ['Z','X','W','U','G','O','F','S','R','N']
if_dic_n = ['0','6','2','4','8','1','5','7','3','9']

# ZERO	Z
# SIX	X
# TWO	W
# FOUR	U
# EIGHT	G
# 	ONE		O
# 	FIVE	F
# 	SEVEN	S
# 	THREE	R
# 	NINE	

def problem():
	pre_process()
	number_letters = raw_input()
	dic_num_c_l = count_letters(number_letters)
	return check_ifs_dics(dic_num_c_l)

def check_ifs_dics(dic_num_c_l):
	numbers_found = []
	while(len(dic_num_c_l.keys()) != 0):
		for inx in range(len(if_dic_l)):
			if len(dic_num_c_l.keys()) == 0:
				break
			let = if_dic_l[inx]
			if dic_num_c_l.has_key(let):
				if all_letters_in_num_is_possible(if_dic_n[inx], dic_num_c_l):
					dic_num_c_l = perfome_take_lett_out(if_dic_n[inx], dic_num_c_l)
					numbers_found.append(if_dic_n[inx])
					break

	if len(dic_num_c_l.keys()) != 0:
		print "Len != 0"
		print dic_num_c_l
	return ''.join(sorted(numbers_found))


def all_letters_in_num_is_possible(num, dic_num_c_l):
	dic_num = full_dic[num]

	dic_ncl_keys = dic_num_c_l.keys()

	for key_n in dic_num.keys():
		if key_n not in dic_ncl_keys:

			return False
	return True


def perfome_take_lett_out(num, dic_num_c_l):
	dic_num = full_dic[num]

	for key_n in dic_num.keys():
		if dic_num_c_l.has_key(key_n):
			if dic_num_c_l[key_n] > 0:
				if dic_num_c_l[key_n] - dic_num[key_n] == 0:
					dic_num_c_l.pop(key_n, None)
				else:	
					dic_num_c_l[key_n] = dic_num_c_l[key_n] - dic_num[key_n]
		else:
			print "error"

	return dic_num_c_l

def count_letters(n_str):
	return populate_key_dic(n_str)

def pre_process():
	for k,v in dic_num.items():
		full_dic[k] = populate_key_dic(v)

def populate_key_dic(n_str):
	n_dic = {}
	for char in n_str:
		if n_dic.has_key(char):
			n_dic[char] += 1
		else: 
			n_dic[char] = 1
	return n_dic




if __name__ == '__main__':
	T = int(raw_input())
	case = 1
	while T>0:
		print "Case #%s: %s" % (case, problem())
		case = case + 1
		T = T - 1


