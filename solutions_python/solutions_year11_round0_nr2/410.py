import sys, os

f = open('B-input.in', 'r')
fout = open('B-out', 'w')
case_cnt = int(f.readline())

def build_opp_dict(dict, content, k, v):
	if dict.has_key(content[k]):
		dict[content[k]].append(content[v])
	else:
		dict[content[k]] = [content[v]]
	return dict

def check_combine(dict, f, s):
	if dict.has_key(f+s):
		return dict[f+s]
	elif dict.has_key(s+f):
		return dict[s+f]
	return 0

def check_opp(dict, li):
	for i in range(len(li) - 1):
		if dict.has_key(li[i]):
			subli = dict[li[i]]
			for el in subli:
				if el == li[-1]:
					return []
	return li
		

for i in range(case_cnt):
	l = f.readline()
	el = l.split()
	
	com_cnt = int(el[0])
	com_dict = {}
	for j in range(com_cnt):
		com_dict[el[j + 1][:-1]] = el[j+1][-1:]
	el = el[com_cnt + 1:]

	opp_cnt = int(el[0])
	opp_dict = {}
	for j in range(opp_cnt):
		opp_dict = build_opp_dict(opp_dict, el[j+1], 0, 1)
		opp_dict = build_opp_dict(opp_dict, el[j+1], 1, 0)
	
	el = el[opp_cnt + 1:]

	string_cnt = int(el[0])
	str = el[1]
	result_list = [str[0]]
	for j in range(1, string_cnt):
		result_list.append(str[j])
		if len(result_list) <= 1:
			continue
		#combine
		r = check_combine(com_dict, result_list[-2], result_list[-1])
		if r != 0:
			result_list = result_list[:-2]
			result_list.append(r)
			continue

		#opp
		result_list = check_opp(opp_dict, result_list)
	
	fout.write('Case #%d: [' % (i + 1))
	for r in result_list[:-1]:
		fout.write('%s, ' % (r,))
	if len(result_list) >= 1:
		fout.write('%s]\n'% (result_list[-1],))
	elif len(result_list) == 0:
		fout.write(']\n')
