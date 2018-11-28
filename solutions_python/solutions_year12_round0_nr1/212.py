import sys
import os

dic = {}
num_cases = 0

def match(file_obj, nc, total, dic):
    """processor"""

    if nc == total+1:
        return

    this_line = file_obj.readline()
    output = ''
    for i in range(len(this_line)):
        output += dic[this_line[i]]


    print 'Case #%s: %s' % (nc,output)
  
    match(file_obj, nc+1, total, dic)

def main(file_path, path2, path3):
    """docstring for main"""
    file_object = open(file_path,'r')
    code_object = open(path2, 'r')
    key_object = open(path3, 'r')
    
    # build dict
    for i in range(3):
        line_code = code_object.readline()
        line_key = key_object.readline()
        for j in range(len(line_code)):
            dic[line_code[j]] = line_key[j]

    dic['q'] = 'z'
    dic['z'] = 'q'
    num_cases = int(file_object.readline())
    match(file_object, 1, num_cases, dic)
    
    
if __name__ == '__main__':
    """docstring for __name__"""
    if(len(sys.argv) == 4):
        main(sys.argv[1], sys.argv[2], sys.argv[3])
            
