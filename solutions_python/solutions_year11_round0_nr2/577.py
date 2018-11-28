#!/usr/bin/python
import sys

def solve(test_case):
	#print test_case
	count = 0
	c = int(test_case[count])
	count += 1
	c_list = []
	while c > 0:
		c_list.append(list(test_case[count]))
		count += 1
		c -= 1
	d = int(test_case[count])
	count += 1
	d_list = []
	while d > 0:
		d_list.append(list(test_case[count]))
		count += 1
		d -= 1
	#print c_list 
	#print d_list
	count += 1
	ele_list = []
	for i in list(test_case[count]):
		if len(ele_list) == 0:
			ele_list.append(str(i))
		else:
			flag = False
			for k in c_list:
				if i == k[0]:
					if ele_list[-1] == k[1]:
						ele_list[-1] = str(k[2])
						flag = True
						break
				elif i == k[1]:
					if ele_list[-1] == k[0]:
						ele_list[-1] = str(k[2])
						flag = True
						break
			if flag:
				continue
			for k in d_list:
				if i == k[0]:
					if k[1] in ele_list:
						del ele_list[:]
						flag = True
				elif i == k[1]:
					if k[0] in ele_list:
						del ele_list[:]
						flag = True
			if flag:
				continue
			ele_list.append(str(i))

	return ', '.join(ele_list)
#Main script---------------------------------------------------------
def main():
	if len(sys.argv) != 2:
		sys.stderr.write("usage: %(self)s 'input'\n"%\
							{'self': sys.argv[0]})
		return

	count = 1
	try:
		f = open(sys.argv[1], 'r')
		for line in f:
			if len(line.split()) == 1:
				continue;
			sys.stdout.write('Case #' + str(count) + ': [' + solve(line.split()) + "]\n")
			count += 1
	finally:
		f.close()
		 

if (__name__ == "__main__"):
	main()