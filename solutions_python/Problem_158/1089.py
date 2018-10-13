def solve(x, r, c):
	x = int(x)
	r = int(r)
	c = int(c)
	if x >= 7:
		return "Richard"
	elif x == 1:
	    return "Gabriel"
	else:
	    if r % x == 0 or c % x == 0:
	        if c >=x-1 and r >= x-1:
	            return "Gabriel"
	        else:
	            return "Richard"
	    else:
	        return "Richard"




def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
len_file = file_len('dsmalltext.txt')


getdata = open('dsmalltext.txt')
getdata.readline().strip()


def make_list():
	long_list = []
	for i in range(len_file -1):
		line = getdata.readline().strip()
		line = line.split(" ")
		long_list.append(line)
	return long_list
long_list = make_list()

for i in range(len(long_list)):
	line = solve(long_list[i][0], long_list[i][1], long_list[i][2])
	print("Case #{0}: {1}".format(i+1, line))





