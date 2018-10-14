'''
Created on Apr 14, 2012

@author: silent
'''

import sys

def get_input(input_file):
    infile = open(input_file)
    return infile

def get_output(output_file):
    outfile = open(output_file, "w")
    return outfile

def get_recycled_numbers_count(a, b):
    result = 0
    
    for num in range(a, b+1):
        if num < 12:
            continue
        
        str_num = str(num)
        recycled_nums = []

        for idx in range(1, len(str_num)):
            str_recycled_num = str_num[idx:] + str_num[:idx]
            
            if str_recycled_num[0] == '0':
                continue
            
            recycled_num = int(str_recycled_num)
            if num == recycled_num:
                break
            if recycled_num in recycled_nums:
                break
            
            if recycled_num > num and recycled_num <= b:
                recycled_nums.append(recycled_num)
                result = result + 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 1:
        input_file = 'input.in'
    else:
        input_file = sys.argv[1]
    filename = input_file.split(".")[0]
    infile = get_input(input_file)
    outfile = get_output(filename + ".out")
    
    t = int(infile.readline())
    
    for case_num in range(t):
        [a, b] = map(int, infile.readline().split())
        
        result = get_recycled_numbers_count(a, b)
        
        outfile.write("Case #%d: %d\n" % (case_num+1, result))
        print "Case #%d: %d" % (case_num+1, result)
    
    infile.close()
    outfile.close()