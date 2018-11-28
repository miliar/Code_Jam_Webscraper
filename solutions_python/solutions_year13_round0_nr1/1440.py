"""
Code jam q. round question 1 
"""
import sys
import numpy

def translate(x):
    if x == '.':
        return 0
    elif x == 'T':
        return 1
    elif x == 'X':
        return 2
    elif x== 'O':
        return 3
    else:
        assert False, 'cant translate %s' % x

def load_tests(path):
    f = file(path)
    num_tests = int(f.readline())
    test_lines = [line.strip() for line in f.readlines() if line.strip()]
    assert 4 * num_tests == len(test_lines) 
    
    tests = []
    i = 0
    while i < len(test_lines):
        test = numpy.array([[translate(x) for x in tline] for tline in test_lines[i: i + 4]])
        tests.append(test)
        i += 4

    return tests

def is_win_vec(vector):
    if 0 in vector:
        return False
    return not numpy.any(vector[0] != vector) 

def check_wins(mat):
    if is_win_vec(mat.diagonal()):
        return True
    
    if is_win_vec(numpy.fliplr(mat).diagonal()):
        return True
    
    for row in mat:
        if is_win_vec(row):
            return True
    
    for col in mat.transpose():
        if is_win_vec(col):
            return True 
    
    return False

def solve(test):
    xs = numpy.copy(test)
    xs[xs == 1] = 2
    xs[xs == 3] = 0
    if check_wins(xs):
        print 'X won'
    else:
        os = numpy.copy(test)
        os[os == 1] = 3
        os[os == 2] = 0
        if check_wins(os):
            print 'O won'
        else:
            if 0 in test:
                print 'Game has not completed'
            else:
                print 'Draw'

def main():
    tests = load_tests(sys.argv[1])
    
    test_num = 1
    for test in tests:
        print 'Case #%d:' % test_num, 
        solve(test)
        test_num += 1
        
if '__main__' == __name__:
    main()
