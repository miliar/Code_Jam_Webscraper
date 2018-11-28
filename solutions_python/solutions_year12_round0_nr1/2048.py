r_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x_list = ['y' ,'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q']

f = open('/Users/jasonherald/Downloads/A-small-attempt1.in.txt', 'r')
f_lines = f.readlines()
ctr = 0

for line in f_lines:
	#string1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
	if (len(line) > 5):
		ctr = ctr + 1
		result = ""

		for c in line:
			if (c != ' ' and c != '\n'):
				result = result + (x_list[r_list.index(c)])
			else:
				result = result + " "
				
		print("Case #" + str(ctr) + ": " + result)