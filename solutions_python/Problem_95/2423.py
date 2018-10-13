#!/usr/bin/python2
def shifr():
	s = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
		rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
		de kr kd eoya kw aej tysr re ujdr lkgc jv"
	x = "our language is impossible to understand\
		there are twenty six factorial possibilities\
		so it is okay if you want to just give up"
	ret = {}
	for i, char_ in enumerate(s):
		ret[char_ ] = x[i]
	ret['q'] = "z"
	ret['z'] = "q"
	ret['\n'] = "\n"
	return ret



input_file = open("input", 'r')
output_file = open("output", 'w')
input_data = input_file.readlines()
#lines = input_data[0]
input_data = input_data[1:]
lines = range(1,len(input_data)+1)
replace_dict = shifr()
ret = []

for number, string_line in enumerate(input_data):
	ret.append(("Case #%d: "%lines[number]) + "".join([replace_dict[x] for x in string_line]))

output_file.write("".join(ret))
input_file.close()
output_file.close()
