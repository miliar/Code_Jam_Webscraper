from iopart import read_input, write_output

raw_data = read_input(name_of_file='A-large.in')
number_of_integers = raw_data[0]
data = (element.split(' ') for element in raw_data[1])
final_answer = []


def flip_to_the_win(pancake_que='-------', flipper_size='7'):
    counter = 0
    flipper_size = int(flipper_size)
    impossible = 'IMPOSSIBLE'
    length = len(pancake_que)
    if ('-' in pancake_que):
        if flipper_size > length:
            return impossible

        position = pancake_que.find('-')
        while(is_fitting(length, position, flipper_size) and (position+1)):
        	happy_slice = slice(position, position + flipper_size)
       		new_sub_string = ''
        	for element in pancake_que[happy_slice]:
        		new_sub_string += (reflect(element))
        	old = pancake_que[happy_slice]
        	pancake_que = pancake_que.replace(old, str(new_sub_string), 1)
        	position = pancake_que.find('-')
        	counter += 1
        if (position + 1):
        	return impossible
        else:
        	return counter

        
    else:
        return counter
    

def reflect(symbol):
	if symbol == '+':
		return '-'
	else:
		return '+'

def is_fitting(length, pos, flipper_size):
	if (length - pos - flipper_size + 1) > 0:
		return True
	else:
		return False


for element in data:
	final_answer.append(flip_to_the_win(pancake_que=element[0], flipper_size=element[1]))

write_output(final_answer, name_of_file = 'A-large.out')



    