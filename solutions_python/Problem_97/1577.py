from sys import stdin
indata = stdin.readlines()

def get_sorted_list(a, b):
	return [x for x in range(a, b+1)]

def right_shift(num_string):
	temp = list(num_string)
	bucket = temp[0]
	for x in range(1,len(num_string)):
		temp[x-1] = temp[x]
	temp[-1] = bucket
	return str(''.join(temp))


def get_combinations(num):
	bucket = []
	num_str = str(num)
	


def get_shifted_values(num):
	bucket = []
	tmp = num
	while(1):
		bucket.append(tmp)
		tmp = right_shift(str(tmp))
		if(str(tmp) == str(num)):
			break
	return bucket
"""	for x in range(1, len(str(num))):
		bucket.append(right_shift(str(tmp)))
		tmp = right_shift(str(tmp))
	return bucket
"""

def get_num(a, b):
	num = 0
	for x in range(a, b+1):
		mods = get_shifted_values(x)
		for y in mods:
			if(int(y) > x and int(y) < b + 1):
				num += 1
	return num

def test():
	for x in range(1, len(indata)):
		num = 0
		indata[x] = indata[x].replace('\n', '').split()
		a = indata[x][0]
		b = indata[x][1]
		print "Case #%d: %d" % (x, get_num(int(a), int(b)))

def main():
	test()
"""
	a = 100
	b = 500
	num = 0
	for x in range(a, b+1):
		mods = get_shifted_values(x)
		for y in mods:
			if(int(y) > x and int(y) < b + 1):
				num += 1
	print num
"""
		
if __name__ == "__main__":
	main()

