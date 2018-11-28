"""
Code jam q. round question 2 
"""
import sys
import numpy

def load_tests(path):
    f = file(path)
    num_tests = int(f.readline())
    tests = []
    for index in xrange(num_tests):
        n, m = [int(x) for x in f.readline().strip().split()]
        test = numpy.array([[int(x) for x in f.readline().strip().split()] for i in xrange(n)], dtype = 'int32')
        assert test.shape == (n, m)
        tests.append(test)
        
    return tests

def solve(mat):
    n, m = mat.shape
    for i in xrange(n):
        for j in xrange(m):
            if (mat[i, j] < mat[i, :].max()) and (mat[i, j] < mat[:, j].max()):
                print 'NO'
                return
    
    print 'YES'

def main():
    tests = load_tests(sys.argv[1])
    
    test_num = 1
    for test in tests:
        print 'Case #%d:' % test_num, 
        solve(test)
        test_num += 1
        
if '__main__' == __name__:
    main()
