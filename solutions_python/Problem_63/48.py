import sys
import math

def test_count(L, P, C):
    steps = math.log(1.0*P / L, C)
    #print L, P, C
    #print " %s" % steps
    #print " %s" % math.log(steps, 2)
    half_steps = math.log(steps, 2)
    count = int(math.ceil(half_steps))
    count = max(0, count)
    return count

def do_one_test_case(file):
    L, P, C = (int(n) for n in file.readline().split())
    return test_count(L, P, C)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline())
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = expected_list[0:-1]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)
