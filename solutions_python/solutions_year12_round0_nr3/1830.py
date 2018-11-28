#!/usr/bin/python2
import re
def check(s1, s2):
	s1 = str(s1)
	s2 = str(s2)
	len_ = len(s2)
	if len_ < 2 or len_ != len(s1):
		return False
	while len_:
		len_ -= 1
		s2 = s2[1:] + s2[0]
		if int(s1) == int(s2):
			return True
		if len < 0:
			return False

def calculate(A, B):
	print A
	print B
	n = int(A)
	m = int(B)
	ret = []
	result = 0
	while n <= m:
		ret.append(n)
		n += 1

	for i,x in enumerate(ret):
		arr = [z for z in ret[i+1:] if check(x, z)]
		result += len(arr)
	return result

input_file = open("input", 'r')
output_file = open("output", 'w')
input_data = input_file.readlines()
#lines = input_data[0]
input_data = input_data[1:]
lines = range(1,len(input_data)+1)

ret = []

for number, string_line in enumerate(input_data):
	numA, numB = re.split("\ ", string_line)
	ret.append(("Case #%d: "%lines[number]) + str(calculate(numA, numB)) + '\n')
print ret
output_file.write("".join(ret))
input_file.close()
output_file.close()


