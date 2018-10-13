import sys

def lowest_number(s):
    translation = {}
    order = range(100)
    order[0] = 1
    order[1] = 0
    n = 0
    for c in s:
        if c not in translation:
            translation[c] = order[n]
	    n += 1

    if n == 1:
        n = 2 # Assumption from question
    seconds = 0
    for c in s:
        seconds = seconds * n + translation[c]
        
    return seconds
            

def do_one_test_case(file):
    s = file.readline().strip()
    return lowest_number(s)

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
