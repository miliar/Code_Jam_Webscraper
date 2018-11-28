#imports
import numpy as np
import os
import argparse

# Function

def reduction(num):
    if len(str(num)) > 1:

        num_str = (str(num))[::-1]
        count = 0

        for i in range(len(num_str)-1):
            if np.int(num_str[i]) >= np.int(str(num_str[i+1])):
                count +=1

        nines = []
        for i in range(count):
            nines.append(str(9))
        new_end = ''.join(nines)
        num_str = new_end + str(np.int(num_str[count])-1) + num_str[count+1:]

        num_str_temp = num_str.replace('-1','9')

        if not num_str is num_str_temp:

            for i in range(len(num_str)-2):
                if num_str[i] == '-':

                    num_str_temp = num_str_temp[:i+1] + str(np.int(num_str_temp[i+1])-1) + num_str_temp[i+2:]

        num_str = num_str_temp
        num = np.int(num_str[::-1])
    return num

def untidy_check(num):
    untidy = False
    for i in range(len(str(num))-1):
        if np.int(str(num)[i]) > np.int(str(num)[i+1]):
            untidy = True

    return untidy

# output = []
# for num in int_content:
#     while(untidy_check(num)):
#         num = reduction(num)
#
#     output.append(num)
#     print num


parser = argparse.ArgumentParser(description='Input file')
parser.add_argument(
	'input',
	type=str,
	help='Path to Input file'
)
parser.add_argument(
	'output',
	type=str,
	help='Path to Output file'
)

args = parser.parse_args()
input_file = args.input
output_file = args.output


cwd = os.getcwd()
fname = cwd + "/" + input_file
with open(fname) as f:
    content = f.readlines()

content = content[1:]
int_content =[]
for item in content:
    int_content.append(np.int(item))

f = open(cwd + '/' + output_file, 'w')

count = 1
for num in int_content:
    while(untidy_check(num)):
        num = reduction(num)

    f.write("Case #" + str(count) + ": " + str(num) + "\n")
    count += 1

f.close()
