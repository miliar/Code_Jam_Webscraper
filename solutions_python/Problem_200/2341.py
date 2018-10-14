#!/usr/bin/python3
import sys

def is_tidy(num):
    # quick tidy checker
    num_str = str(num)
    prev = 0
    for char in list(num_str):
        digit = int(char)
        if digit >= prev:
            prev = digit
            continue
        else: return False
    return True

def find_tidy(num):
    # brute force. Dumb, but good for testing
    for i in range(int(num),0,-1):
        if is_tidy(i):
            return i

def quick_find_tidy(num):
    # walk throught then number and find where it fails
    prev = 0
    order = len(num)
    for char in list(num):
        digit = int(char)
        if digit >= prev:
            prev = digit
            order = order - 1
            continue
        else:
            # fails
            prefix_num = int(num[0:len(num)-order]) - 1
            suffix_num = int(10**(order)) - 1

            return quick_find_tidy("%s%s" % (prefix_num, suffix_num))
    return num
    
def test():
    num_tests = None
    i = 1
    for line in sys.stdin:
        if not num_tests:
            num_tests = int(line.strip())
            continue
        print("Case #%s: %s" % (i, int(quick_find_tidy(line.strip()))))
        i = i + 1

    assert i-1 == num_tests, "Unexpected number of tests (expected %s, got %s)" % (num_tests, i)
    
if __name__ == "__main__":
#    print(int(quick_find_tidy(sys.argv[1])))
    test()
