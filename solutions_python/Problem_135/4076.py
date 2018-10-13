def checking_both_arrays(the_first_Array, the_second_Array):
	count = 0
	answer = 0

	for i in the_first_Array:
		for j in the_second_Array:
			if i == j:
				count += 1
				answer = i

	if answer == 0:
		return "Volunteer cheated!"

	elif count > 1:
		return "Bad magician!"

	else:
		return answer

def magic_trick(first_array, second_array, first, second):

	answer1 = int(first) -1

	the_first_Array = first_array[answer1]

	answer2 = int(second) - 1

	the_second_Array = second_array[answer2]

	return checking_both_arrays(the_first_Array, the_second_Array)



f = open ('in.in' , 'r')
list = [ map(int,line.split(' ')) for line in f ]

list.pop(0)
new_list = []
count = 0
while count < len(list):
	popped = list.pop(count)
	count += 4
	new_list.append(popped[0])

my_list = []

for i in xrange(0, len(list), 4):
        result = list[i:i+4]
        my_list.append(result)

first_index = 0
second_index = 1
case_number = 0

count = 0

f = open('output.out', 'w+')

while (count < len(my_list)/2):
	final_result = magic_trick(my_list[first_index], my_list[second_index], new_list[first_index], new_list[second_index])
	first_index += 2
	second_index += 2
	case_number += 1
	count += 1
	string_file = "Case #%s: %s\n" % (case_number, final_result)

	f.write(string_file)

