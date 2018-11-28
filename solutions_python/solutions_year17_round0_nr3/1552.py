import math
from collections import deque

def odd_gap(number):
	gap1 = (number-1)/2
	gap2 = (number-1)/2
	return (gap1, gap2)
# gap1 > gap2
def even_gap(number):
	gap1 = number/2
	gap2 = number/2-1
	return gap1, gap2


def test (n,k):
	# n is the size of space
	gap_list = [None]*n
	gap_list[0] = n
	max_number=0
	min_number=0
	index_to_add = 1
	for index_to_read in range(n):
		origin_space = gap_list[index_to_read]
		#print type(origin_space)
		#print origin_space
		if origin_space==1:
			continue
		elif origin_space%2 ==1:
			gap1, gap2 = odd_gap(origin_space)
			gap_list[index_to_add] = gap1
			gap_list[index_to_add+1] = gap2
			# update index
			index_to_add = index_to_add +2

		elif origin_space==2:
			gap_list[index_to_add] = 1
			# update index
			index_to_add = index_to_add +1

		else:
			gap1, gap2 = even_gap(origin_space)
			gap_list[index_to_add] = gap1
			gap_list[index_to_add+1] = gap2
			# update index
			index_to_add = index_to_add +2

	gap_list = sorted(gap_list, key=int, reverse=True)
	space_for_the_person = gap_list[k-1]
	if space_for_the_person%2 ==1:
		max_, min_ = odd_gap(space_for_the_person)
	else:
		max_, min_ = even_gap(space_for_the_person)
	#print gap_list
	return str(max_) + " " + str(min_)



case_num = 1
input_path = "../Downloads/C-small-2-attempt3.in"
out = open('answer.txt', 'w')
with open(input_path) as f:
    lines = f.readlines()
    lines_head = lines[0]
    lines_body = lines[1:]
    for element in lines_body:
	    input_element =  element.rstrip() # remoce \n
	    input_element_array = input_element.split()
	    number = test(int(input_element_array[0]), int(input_element_array[1]))
	    answer = "Case #"+ str(case_num) +": "+ number
	    print(answer)
	    out.write(answer+'\n')
	    case_num = case_num +1

out.close()