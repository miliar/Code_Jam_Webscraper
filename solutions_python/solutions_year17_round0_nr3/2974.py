import sys
from collections import defaultdict


def calculate_right_distance(i, arr):
	right = 0
	j = i + 1
	len_arr = len(arr)
	while j < len_arr:
		if arr[j] == 0:
			right += 1
		else:
			return right
		j = j + 1
	return right


def calculate_left_distance(i, arr):
	left = 0
	j = i - 1
	while j > 0:
		if arr[j] == 0:
			left += 1
		else:
			return left
		j = j - 1
	return left

def get_selected_index(min_d, max_d, output):
	min_dis = max(min_d.keys())
	max_dis = max(max_d.keys())
	min_index = min_d[min_dis]
	max_index = max_d[max_dis]
	selected_index = -1
	if len(min_index) > 1:
		index_list = []
		max_list = []
		for v in min_index:
			i,min_dis,max_dis = output[v]
			max_list.append(max_dis)
			index_list.append(i)

		max_val = max(max_list)
		selected_index = min(set(index_list).intersection(set(max_d[max_val])))
	else:
		selected_index = min_index[0]
	
	return selected_index


def find_distance_both_sides(n,k):
	arr = [0]*(n+2)
	arr[0] = 1
	arr[-1] = 1
	all_ppl = []
	for k in range(0,k):
		min_d = defaultdict(list)
		max_d = defaultdict(list)
		output = defaultdict(tuple)

		for i in range(1,n+2):
			if arr[i] != 1:
				left = calculate_left_distance(i, arr)
				right = calculate_right_distance(i,arr)
				min_dis = min(left,right)
				min_d[min_dis].append(i)
				max_dis = max(left, right)
				max_d[max_dis].append(i)
				output[i] = (i,min_dis,max_dis)
			else:
				continue
		
		selected_index = get_selected_index(min_d, max_d, output)
		arr[selected_index] = 1
		all_ppl.append(output[selected_index])
	return all_ppl.pop()

if __name__ == '__main__':
	f = open('C:\Users\sdhupar\Downloads\C-small-1-attempt3.in')
	line_cnt = 0
	inpts = []
	test_case = 0
	for line in f:
		if line_cnt == 0:
			test_case = int(line)
			line_cnt += 1
		else:
			inpts.append(line.rstrip('\n').split(' '))
	for i in range(test_case):
		n, k = long(inpts[i][0]), long(inpts[i][1])
		j,min_dis,max_dis  = find_distance_both_sides(n,k)
		print "Case #"+str(i+1)+": "+str(max_dis)+" "+str(min_dis)