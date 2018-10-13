import sys

input_file = open(sys.argv[1], 'r')

file_lines = map(str.strip, input_file.readlines())

T = int(file_lines[0])

def reverse_int(n):
    return int(str(n)[::-1])

def is_palindrome(n):
    return n == reverse_int(n)

global_max = 0
dict = {}

def update_dict(max):
    for i in range(global_max,max):
        if is_palindrome(i) and i*i <= max:
            m = i*i
            if is_palindrome(m):
                dict[m] = i


for i in range(1, T+1):
    c = 0
    line = file_lines[i].split()
    min = int(line[0])
    max = int(line[1])
    if max > global_max:
        update_dict(max)
    
    for d in dict.keys():
        if d >= min and d <= max:
            c += 1
    
    print 'Case #%d: %d'%(i, c)
