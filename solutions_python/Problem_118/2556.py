import sys
import math

input_file_name = 'input2.txt'
output_file_name = 'output2.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

def pal(n):
    num = n
    rev = 0
    while (num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num, mod = divmod(num,10)
    if n == rev:
        return 1
    return 0

def sqrpal(n):
    root = math.sqrt(n)
    if root.is_integer():
        if pal(root):
            return 1
    return 0

contents = f_in.readlines()

num_cases = int(contents.pop(0))

for case_num in range(num_cases):

    count = 0
    line = contents.pop(0)
    b, e = line.split()
    begin = int(b)
    end = int(e)

    for number in range(begin,end+1):
        if pal(number) and sqrpal(number):
            count = count + 1
            
    print('Case #{}: {}'.format(case_num + 1, count))
    print('Case #{}: {}'.format(case_num + 1, count), file = f_out)
    
f_in.close()
f_out.close()
