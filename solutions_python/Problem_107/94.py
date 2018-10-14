import sys

num_case = int(sys.stdin.readline())

def divde_and_merge(box, toy):
	if box == [] or toy == []:
		return 0
	else:
		if box[1] == toy[1]:
			if (box[0] == toy[0]):
				return box[0]+divde_and_merge(box[2:],toy[2:])
			elif (box[0] > toy[0]):
				box[0] -= toy[0]
				return toy[0]+divde_and_merge(box,toy[2:])
			else:
				toy[0] -= box[0]
				return box[0]+divde_and_merge(box[2:],toy)
		else:
			return max(divde_and_merge(box[2:],toy), divde_and_merge(box, toy[2:]))

for cur_case in range(1, num_case+1):
	num_pair_box_stay = 0
	num_pair_toy_stay = 0
	[num_box, num_toy] = [int(w) for w in sys.stdin.readline().strip('\n').split(' ')]
	box_list = map(int,sys.stdin.readline().strip('\n').split(' '))
	toy_list = map(int,sys.stdin.readline().strip('\n').split(' '))
			
	# print out final result
	file = open('output.txt', 'a')
	# Uniqueness of the result
	file.write('Case #%d: %d\n'%(cur_case, divde_and_merge(box_list,toy_list)))