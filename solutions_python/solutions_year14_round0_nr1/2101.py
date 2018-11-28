import sys
import pdb

def check(list1, list2):
	#pdb.set_trace()
	counter = 0
	for i in list1:
		if i in list2:
			counter = counter +1
			value = i
		if counter >1:
			return (False, 0)
	if counter == 0:
		return (False,1)
	return (True, value)

def read_data(file_obj):
	row = int(file_obj.readline())
	list1 = None
	for i in range(4):
		temp = file_obj.readline()
		if i == row-1:
			list1 = temp.split()
	return list1


def parse_data(directory):
	f = open(directory,"r")
	output = open('output.txt','w')
	cases = int(f.readline())
	for i in range(cases):
		list1 = read_data(f)
		list2 = read_data(f)
		result = check(list1, list2)
		if result[0] == False:
			if result[1] == 0:
				to_output = "Bad magician!"
			if result[1] == 1:
				to_output = "Volunteer cheated!"
		else:
			to_output = result[1]

		out_string = "Case #%d: %s\n" %(i+1, to_output)
		output.writelines(out_string)

	f.close()
	output.close()

if __name__ == '__main__':
	directory = sys.argv[1]
	print type(directory)
	parse_data(directory)