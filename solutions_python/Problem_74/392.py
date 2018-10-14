import sys, os

f = open('A-input.in', 'r')
fout = open('A-output', 'w')

test_cnt = int(f.readline())

#step include final push operation
def cal_distance(dict, cnt):
	previous = 1
	for i in range(cnt):
		if dict.has_key(i):
			p = dict[i]
			dict[i] = abs(previous - dict[i]) + 1 # postion to steps 
			previous = p
	return dict
	

for i in range(test_cnt):
	l = f.readline()
	el = l.split()
	step_cnt = int(el[0])

	O_dict = {}
	B_dict = {}
	total_cnt = 0
	O_previous = 0
	B_previous = 0

	# record
	for j in range(step_cnt):
		if el[j * 2 + 1] == 'O':
			O_dict[j] = int(el[j * 2 + 2])
		else:
			B_dict[j] = int(el[j * 2 + 2])
	
	O_dict = cal_distance(O_dict, step_cnt)
	B_dict = cal_distance(B_dict, step_cnt)

	for j in range(step_cnt):
		if O_dict.has_key(j):
			if (O_previous + O_dict[j]) > total_cnt:
				total_cnt = O_previous + O_dict[j]
			else:
				total_cnt += 1
			O_previous = total_cnt
		else:
			if (B_previous + B_dict[j]) > total_cnt:
				total_cnt = B_previous + B_dict[j]
			else:
				total_cnt += 1
			B_previous = total_cnt
	
	fout.write('Case #%d: %d\n' % (i+1, total_cnt))

f.close()
fout.close()
