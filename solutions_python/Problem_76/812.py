import sys
import os

path = os.path.abspath(sys.argv[1])
with open(path) as test_file:
    t = int(test_file.readline().strip())
    i = 1
    while t > 0:
        n = int(test_file.readline().strip())
        case = test_file.readline().strip().split()
        case = list(int(e) for e in case)
        input_sum = sum(case)
       
        rf = reduce(lambda x, y : x ^ y, case)
        sm = sys.maxint
        for e in case:
            if e < sm: sm = e
        print 'Case #%d: %s' % (i, str(input_sum - sm) if rf == 0 else 'NO')
        t -= 1
        i += 1
    
