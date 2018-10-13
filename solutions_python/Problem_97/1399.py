import math

def get_num_pairs(a, b, array):
	length = len(str(b))
	arr_len = len(array)

	pairs = {}
	test = array.popitem()

	while test:
	    j = 1
	    while j < length:
		remainder = test[0]%(10**j)

		swapped = remainder*(10**(length-j))+int(test[0]/(10**j))
		arr_len=len(array)
		if array.has_key(swapped):		
		#if find(swapped, array, 0, arr_len-1) > 0:
		    pair = [test, swapped]
		    pair = str(test)+str(swapped)
		    pairs[pair]=1

	    	j += 1

	    if len(array) != 0:
		test = array.popitem()
	    else:
		break


	return len(pairs)



def find(swapped, array, head, tail):	
	if tail < head:
	    return -1

	mid = (head + tail) / 2
	if mid == 0:
	    if array[mid] == swapped:
		return 1
	    else:
		return -1
	if array[mid] == swapped:
	    return 1
	elif array[mid] > swapped:
	    return find(swapped, array, head, mid-1)
	else:
	    return find(swapped, array, mid+1, tail)

filename = 'C-large.in'
out_file = 'output.txt'
text = open(filename, "r")

line_counter = 1
output = ''

linecount = 1
for line in text:
	array = {}
	recycle_count = 0

	if line_counter == 1:
	    testcase_num = int(line)
	else:
	    linecount += 1
	    output += 'Case #'+str(line_counter-1)+': '
	    numbers = line.split()

	    a = int(numbers[0])
	    b = int(numbers[1])

	    if b <= 20:
		output += '0' + '\n'
		line_counter += 1
		continue
	
	    x = a

	    for i in range(b-a+1):
		array[x] = x
		x += 1
	    

	    recycle_count += get_num_pairs(a, b, array)
		

	    output += str(recycle_count)+'\n'

	line_counter += 1

#print output

out = open(out_file, "w")
out.write(output)

