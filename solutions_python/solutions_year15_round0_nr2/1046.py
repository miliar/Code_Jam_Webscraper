from collections import Counter
#input_lines = open("sub-8.in").read().splitlines()
#input_lines = open("A-small-attempt0.in").read().splitlines()
#input_lines = open("A-large-attempt0.in").read().splitlines()
input_lines = open("B-small-attempt5.in").read().splitlines()
#input_lines = open("B-large-attempt0.in").read().splitlines()
#input_lines = open("C-small-attempt0.in").read().splitlines()
#input_lines = open("C-large-attempt0.in").read().splitlines()
#input_lines = open("D-small-attempt0.in").read().splitlines()
#input_lines = open("D-large-attempt0.in").read().splitlines()

test_num = int(input_lines[0])

def func(counter_object, tmp_cnt):
	keys = counter_object.keys()
	max_p = max(keys)
	
	if max_p < 4:
		return tmp_cnt + max_p 
	
	if max_p == 4 and counter_object[max_p] == 1 and not 3 in keys:
		return tmp_cnt + 3
	elif max_p == 4:
		return tmp_cnt + 4

	val = counter_object.pop(max_p)
	func_list = [0] * (max_p/2-1)
	for i in range(2,max_p/2+1):
		tmp_counter_object = Counter(counter_object)
		tmp_counter_object[i] += val
		tmp_counter_object[max_p-i] += val
		func_list[i-2] = func(tmp_counter_object,tmp_cnt+val)
	return min([max_p+tmp_cnt]+func_list)

for i in range(test_num):
	d = input_lines[2*i+1]
	p = map(int, input_lines[2*i+2].split())
	p_cnt = Counter(p)
	cnt = func(p_cnt,0) 
	print "Case #" + str(i+1) + ": " + str(cnt)
