def first_method(case):
	eaten_shrooms = 0
	placed_shrooms = 0
	for i in range(len(case) -1):
		first = int(case[i])
		second = int(case[i+1])
		if first > second:
			eaten_shrooms += (first - second)
		else:
			placed_shrooms += (second - first)
	return eaten_shrooms


def second_method(case):
	length_case = 0
	max_shrooms = 0
	eaten_shrooms = 0
	for i in range(len(case) -1):
		first = int(case[i])
		second = int(case[i+1])
		if first > second:
			if max_shrooms < (first - second):
				max_shrooms = (first - second)
	for i in range(len(case) -1):
		first = int(case[i])
		if first <= max_shrooms:
			eaten_shrooms += first
		else:
			eaten_shrooms += max_shrooms

	return eaten_shrooms


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
len_file = file_len('sexytext.txt')


getdata = open('sexytext.txt')
getdata.readline().strip()


def make_list():
	long_list = []
	for i in range(len_file -1):
		line = getdata.readline().strip()
		line = line.split(" ")
		long_list.append(line)
	return long_list
new_list = make_list()
long_list = []
for i in range(len(new_list)):
	if i % 2 != 0:
		long_list.append(new_list[i]) 
# for i in range(len(long_list)):
# 	if i 

for i in range(len(long_list)):
	line = first_method(long_list[i])
	second_line = second_method(long_list[i])
	print("Case #{0}: {1} {2}".format(i+1, line, second_line))


