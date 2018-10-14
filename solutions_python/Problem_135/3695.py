#!/usr/bin/python3
def get_row_items(f, index):
	i = 0
	arr = None
	while i < 4:
		if i + 1 == index:
			arr = f.readline().split()
		else:
			f.readline()
		i += 1
	return arr

def check_arrays(first, second, round):
	i = 0
	target = ''
	for item in first:
		if item in second:
			target = item
			i += 1
	if i == 0:
		print('Case #' + str(round) + ': ' + 'Volunteer cheated!')
	elif i == 1:
		print('Case #' + str(round) + ': ' + target)
	elif i > 1:
		print('Case #' + str(round) + ': ' + 'Bad magician!')

def do_magic(f, i):
	first_row = int(f.readline())
	first_row_items = get_row_items(f, first_row)
	second_row = int(f.readline())
	second_row_items = get_row_items(f, second_row)
	check_arrays(first_row_items, second_row_items, i)

f = open("/tmp/test")
cases = int(f.readline())
for i in range(cases):
	do_magic(f, i + 1)
