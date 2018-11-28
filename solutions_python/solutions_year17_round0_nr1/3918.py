#! /usr/bin/python3
def allpositive(outplist):
	flag = 0
	for i in outplist:
		if i == 1:
			flag = flag + 1
	if flag == len(outplist):
		return True

def toggle(inplist):
	outplist = []
	for i in inplist:
		if i == 1:
			outplist.append(0)
		else:
			outplist.append(1)
	return outplist

def iterativeflip(cust_list,flipping_count,flipping):
	flag = 0
	i_position = 0
	rem_values = 0
	i = 0
	try:
		while True:
			if cust_list[i] == 0:
				if i != len(cust_list)-1:
					if i+flipping <= len(cust_list)-1:
						cust_list[i:i+flipping] = toggle(cust_list[i:i+flipping])
						#print(cust_list)
						flipping_count = flipping_count + 1
						break;
					else:
						i_position = len(cust_list)-i
						rem_values = flipping - i_position
						cust_list[i-rem_values:] = toggle(cust_list[i-rem_values:])
						#print(cust_list)
						flipping_count = flipping_count + 1
						break;
				else:
					cust_list[i-flipping+1:]= toggle(cust_list[i-flipping+1:])
					#print(cust_list)
					flipping_count = flipping_count + 1
					break;
			else:
				i = i + 1
	
		if allpositive(cust_list):
				return flipping_count
		else:
			flipping_count = iterativeflip(cust_list,flipping_count,flipping)
			return flipping_count
	except RuntimeError as e:
		#print(e)
		return "IMPOSSIBLE"

def checkflip(d):
	str_in = d[0]
	flipping = int(d[1])
	str_list = list(str_in)
	cust_list = []
	modi_list = []
	flipping_count = 0
	for i in str_list:
		if i == '+':
			cust_list.append(1)
		else:
			cust_list.append(0)
	f = 0
	for i in str_list:
		if i == '+':
			f = f + 1
	if f == len(str_list):
		return 0
	else:
		flipping_count = iterativeflip(cust_list,flipping_count,flipping)
	return flipping_count

def main():
	number_test_cases = int(input())
	flag = 1
	z_input = []
	for i in range(number_test_cases):
		s = raw_input()
		d = s.split(' ')
		z_input.append(d)
	for i in z_input:
		x = checkflip(i)
		print("Case #{}: {}".format(flag,x))
		flag = flag + 1


if __name__ == '__main__':
	main()