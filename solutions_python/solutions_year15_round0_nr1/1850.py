def count_friends(case):
	audience = []
	for i in range(len(case)):
		audience.append(int(case[i]))
	friends = 0
	total = 0
	num_audience_members = sum(audience)
	for i in range(len(audience)):
		total += (audience[i])
		if total < (i+1):
			added_guests= ((i+1) - total)
			friends += added_guests
			total += added_guests
	return friends




def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
len_file = file_len('large.txt')


getdata = open('large.txt')
getdata.readline().strip()


def make_list():
	long_list = []
	for i in range(len_file -1):
		line = getdata.readline().strip()
		line = line.split(" ")
		long_list.append(line[1])
	return long_list
long_list = make_list()

for i in range(len(long_list)):
	line = count_friends(long_list[i])
	print("Case #{0}: {1}".format(i+1, line))


