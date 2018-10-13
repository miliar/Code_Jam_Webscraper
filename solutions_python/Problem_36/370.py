import sys
import re

def get_combinations(letters, message):
    if len(message) == 0:
	return 1
    if len(letters) == 0:
        return 0
    if (message[0] == letters[0]):
        return (get_combinations(letters[1:], message[1:]) + 
                get_combinations(letters[1:], message)) % 10000
    else:
        return get_combinations(letters[1:], message)

def do_one_test_case(f):
    s = f.readline().strip()
    return '%04d' % (get_combinations(s, 'welcome to code jam') % 10000)

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline().strip())
    sys.stderr.write('Cases: %d\n' % cases)
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
        sys.stderr.write('%d of %d done\n' % (i+1, cases))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = [line.strip()+'\n' for line in expected_list[0:-1]]
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
