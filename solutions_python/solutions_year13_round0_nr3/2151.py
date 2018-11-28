import sys

def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__

def process_file(path):
    with open(path, 'r') as file_handle:
        test_count = int(file_handle.readline())
        test_case_list = []

        for i in xrange(test_count):
            test_case = map(int, file_handle.readline().strip().split())
            test_case_list.append(test_case)

        return test_case_list


def is_palindrome(number):
    number_string_list = str(number)
    return number_string_list == number_string_list[::-1]

@memodict
def check_number(number):
    return is_palindrome(number) and is_palindrome(number ** 2)

def process_test_case(test_case):
    min_root = test_case[0] ** 0.5
    if int(min_root) < min_root:
        min_root = int(min_root) + 1
    else:
        min_root = int(min_root)

    max_root = int(test_case[1] ** 0.5)

    results =  [root for root in xrange(min_root, max_root+1) if check_number(root)]
    #print (results, [r**2 for r in results])
    return len(results)

if __name__ == '__main__':
    test_case_list = process_file(sys.argv[1])
    for i, test_case in enumerate(test_case_list):
        print 'Case #{}:'.format(i+1), process_test_case(test_case)
        #process_test_case(test_case)
