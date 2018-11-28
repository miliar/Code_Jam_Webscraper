'''
Created on Apr 13, 2012

@author: karnr
'''

def _parse_input(input_file):
    fh = open(input_file)
    num_of_tests = int(fh.readline().strip())
    count = 1
    test_data = dict()
    while (count <= num_of_tests):
        test_data[count] = map(int, fh.readline().strip().split())
        count += 1
        
    fh.close()
    return test_data

def is_palindrome(x):
    sx = str(x)
    return sx == sx[::-1]

psquares = list()

def find_palindromic_squares(limit):
    global psquares
    for i in xrange(1, limit):
        if not is_palindrome(i):
            continue
        s = i * i
        if is_palindrome(s):
            psquares.append(s)
    

def _execute_test(test_input):
    global psquares
    return len(filter(lambda x: x >= test_input[0] and x <= test_input[1], psquares))

def main():
    test_data_set = _parse_input("test_input")
    num_of_tests = len(test_data_set.keys())
    find_palindromic_squares(10000000)
    output = open("test_output", "w")
    for test_id in xrange(1, num_of_tests + 1):
        test_data = test_data_set[test_id]
        test_result = _execute_test(test_data)
        output.write("Case #%s: %s\n" % (test_id, test_result))
        
    output.close()
    
if __name__ == '__main__':
    main()