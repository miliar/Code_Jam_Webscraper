import numpy as np
import argparse
import os

N = 5
K = 1

content = [[4,2],[5,2],[6,2],[1000,1000],[1000,1]]
output = []

def distribute(N,K):
    bathrooms = pow(10,N+1)+1
    # print(bathrooms)
    Ls = 0
    Rs = 0
    for n in range(K):

        bathroom_list = list(str(bathrooms))

        new_list = []

        for i in range(len(bathroom_list)-1):
            if bathroom_list[i] == '1':
                zero_count = 0
                current_num = '1'

                while(bathroom_list[i+zero_count+1] == '0'):
                    current_num += '0'
                    zero_count += 1
                new_list.append(current_num)

        new_list.append('1')
        new_list = (np.sort(new_list))[::-1]

        largest = new_list[0]
        zeros = len(str(largest))-1

        if zeros%2 == 0:
            largest = largest[:zeros/2] + "1" + largest[zeros/2+1:]
            Ls = zeros/2 -1
            Rs = zeros/2
        else:
            largest = largest[:np.int(zeros/2)+1] + "1" + largest[np.int(np.ceil(zeros/2))+2:]
            Ls = np.int(zeros/2)
            Rs = np.int(zeros/2)

        new_list[0] = largest
        new_num = np.int(''.join(new_list))
        bathrooms = new_num

    max_space = max(Ls,Rs)
    min_space = min(Ls,Rs)
    return max_space, min_space




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
item_list = []

for item in content:
    items = item.split()
    item_list.append([np.int(items[0]), np.int(items[1])])

for item in item_list:
    N = np.int(item[0])
    K = np.int(item[1])
    output.append(distribute(N,K))

f = open(cwd + '/' + output_file, 'w')

count = 1
for item in item_list:
    N = np.int(item[0])
    K = np.int(item[1])
    space_max, space_min = distribute(N,K)

    f.write("Case #" + str(count) + ": " + str(space_max) + " " + str(space_min) + "\n")
    count += 1

f.close()
