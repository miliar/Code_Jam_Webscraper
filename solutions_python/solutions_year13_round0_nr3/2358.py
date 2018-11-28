import sys
import math
import time
    
def get_next_sqrt(a):
    return long(2 * math.sqrt(a) + a + 1)

def is_perfect_square(num):
    square_root = long(math.sqrt(num))
    return num == square_root * square_root
    
def is_palindrome(num):
    rep = str(num)
    result = rep == rep[::-1]
    return result
    
def is_fs(num):
    square_root = long(math.sqrt(num))
    if not num == (square_root * square_root):
        return False
    if not is_palindrome(num):
        return False
    if not is_palindrome(square_root):
        return False
    return True

def get_interval_fs_count(a, b):
    fs_count = 0
    current_number = a
        
    while current_number <= b:
        if is_fs(current_number):
            fs_count += 1
            
        if is_perfect_square(current_number):
            current_number = get_next_sqrt(current_number)
        else:
            current_number += 1
            
    return fs_count
    
    
def main(args):
    filename = args[0]
    with open(filename, 'rb') as f:
        contents = f.readlines()
    out_file = open('fs_out.txt', 'wb')
        
    test_cases_count = int(contents[0].strip())
    test_case_index = 1
    
    for line in contents[1:]:
        stripped = line.strip()
        if not stripped:
            continue
            
        a, b = stripped.split()
        a = long(a)
        b = long(b)
        
        count = get_interval_fs_count(a, b)
        
        result_string = 'Case #%d: %d' % (test_case_index, count)
        if test_case_index != test_cases_count:
            result_string += '\n'
        out_file.write(result_string)
        
        test_case_index += 1

    out_file.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print 'Usage mothafucka'