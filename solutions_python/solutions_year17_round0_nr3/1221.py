'''
def update_list(lst):
	for i in range(0,len(lst)):
		if lst[i]['Empty']:
			count = 0
			index = i - 1
			while index > 0:
				if lst[index]['Empty']:
					count += 1
					index -= 1
				else:
					break
			lst[i]['Ls'] = count
			count = 0
			index = i + 1
			while index < len(lst):
				if lst[index]['Empty']:
					count += 1
					index += 1
				else:
					break
			lst[i]['Rs'] = count
	return

def update_list_fast(lst):
	count = 0
	for i in range(0,len(lst)):
		if not lst[i]['Empty']:
			count = 0
		if lst[i]['Empty']:
			lst[i]['Ls'] = count
			count += 1
	count = 0
	for i in range(len(lst)-1,-1,-1):
		if not lst[i]['Empty']:
			count = 0
		if lst[i]['Empty']:
			lst[i]['Rs'] = count
			count += 1
	return

def update_list_due_to_i(lst, i):
	index = i - 1
	count = 0
	while index > 0:
		if lst[index]['Empty']:
			lst[index]['Rs'] = count
			count += 1
			index -= 1
		else:
			break
	index = i + 1
	count = 0
	while index < len(lst):
		if lst[index]['Empty']:
			lst[index]['Ls'] = count
			count += 1
			index += 1
		else:
			break

def getNextChoiceIndex(lst):
	min_S = 0
	max_S = 0
	index = 1
	for i in range(0,len(lst)):
		if min(lst[i]['Ls'], lst[i]['Rs']) > min_S:
			min_S = min(lst[i]['Ls'], lst[i]['Rs'])
			max_S = max(lst[i]['Ls'], lst[i]['Rs'])
			index = i
		if min(lst[i]['Ls'], lst[i]['Rs']) == min_S:
			if max(lst[i]['Ls'], lst[i]['Rs']) > max_S:
				min_S = min(lst[i]['Ls'], lst[i]['Rs'])
				max_S = max(lst[i]['Ls'], lst[i]['Rs'])
				index = i
	return index

def stalls(n, k):
	#n = 10
	lst = []
	lst.append({'Empty': False, 'Ls': 0, 'Rs': 0})
	for i in range(0,n):
		lst.append({'Empty': True, 'Ls': 0, 'Rs': 0})
	lst.append({'Empty': False, 'Ls': 0, 'Rs': 0})
	update_list_fast(lst)
	#print (lst)
	for i in range(0,k-1):
		index = getNextChoiceIndex(lst)
		lst[index] = {'Empty': False, 'Ls': 0, 'Rs': 0}
		update_list_due_to_i(lst, index)
	index = getNextChoiceIndex(lst)
	#print (lst)
	return max(lst[index]['Ls'], lst[index]['Rs']), min(lst[index]['Ls'], lst[index]['Rs'])


#print(stalls(4,2))
#print(stalls(5,2))
#print(stalls(6,2))
#print(stalls(1000,1000))
#print(stalls(1000,1))
#print(stalls(1000000,1))

def getNextChoiceIndex_faster(lst):
	max_dist = 0
	index = 1
	for i in range(0,len(lst)):
		if lst[i]['dist'] > max_dist:
			max_dist = lst[i]['dist']
			index = i
	return index + math.ceil(max_dist/2), index, max_dist

def getNextChoiceIndex_fastest(lst):
	max_dist = 0
	index = 1
	i = 0
	while i < len(lst):
		if lst[i]['dist'] > max_dist:
			max_dist = lst[i]['dist']
			index = i
		i += lst[i]['dist'] + 1
	return index + math.ceil(max_dist/2), index, max_dist

def update_list_due_to_i_faster(lst, i, initial, max_dist):
	lst[initial]['dist'] = i - initial - 1
	lst[i] = {'Empty': False, 'dist': initial + max_dist - i}

import math

def stalls_faster(n, k):
	#n = 10
	lst = []
	# dist is distance to next non-empty stall
	lst.append({'Empty': False, 'dist': n})
	for i in range(0,n):
		lst.append({'Empty': True, 'dist': 0})
	lst.append({'Empty': False, 'dist': 0})
	#print (lst)
	for i in range(0,k-1):
		index, initial, dist = getNextChoiceIndex_fastest(lst)
		update_list_due_to_i_faster(lst, index, initial, dist)
	index, initial, dist = getNextChoiceIndex_fastest(lst)
	#print (lst)
	return dist - math.ceil(dist/2), math.ceil(dist/2) - 1

#print(stalls_faster(4,2))
#print(stalls_faster(5,2))
#print(stalls_faster(6,2))
#print(stalls_faster(1000,1000))
#print(stalls_faster(1000,1))
#print(stalls_faster(1000000,1))
'''
import math
def stalls_fastest(n,k):
	dists = [n]
	for i in range(0,k-1):
		max_dist = dists.pop(dists.index(max(dists)))
		dists.append(max_dist - math.ceil(max_dist/2))
		dists.append(math.ceil(max_dist/2) - 1)
	print (dists)
	max_dist = dists.pop(dists.index(max(dists)))
	return max_dist - math.ceil(max_dist/2), math.ceil(max_dist/2) - 1

def stalls_heap(n,k):
	lst = []
	index = k
	while index != 0:
		lst.append(index)
		index = math.floor(index/2)
	max_dist = n
	print(lst)
	for i in range(len(lst)-1, 0, -1):
		print (max_dist)
		if lst[i-1] == lst[i]*2:
			max_dist = max_dist - math.ceil(max_dist/2)
		else:
			max_dist = math.ceil(max_dist/2) - 1
	print(max_dist)
	return max_dist - math.ceil(max_dist/2), max(math.ceil(max_dist/2) - 1,0)

def stalls_new_fastest(n,k):
	lst = [n]
	iterations = math.floor(math.log(k,2))
	for i in range(0,iterations):
		new_lst = []
		while len(lst) > 0:
			dist = lst.pop()
			new_lst.append(dist - math.ceil(dist/2))
			new_lst.append(math.ceil(dist/2) - 1)
		lst = new_lst
	lst.sort(reverse=True)
	#print (lst)
	max_dist = lst[k - 2**iterations]
	return max_dist - math.ceil(max_dist/2), max(math.ceil(max_dist/2) - 1,0)

#print(stalls_fastest(500,3))
#print(stalls_new_fastest(500,3))
#[248, 124, 62, 31, 15, 7, 3, 1]
#print(stalls_fastest(697, 667))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  test_case = str(input())
  lst = test_case.split()
  max_S, min_S = stalls_new_fastest(int(lst[0]), int(lst[1]))
  print("Case #{}: {} {}".format(i, max_S, min_S))