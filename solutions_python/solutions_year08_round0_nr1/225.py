import sys

def switch_count(engines, searches):
    switches = 0
    unused = set(engines)
    for s in searches:
        if s in unused:
            unused.remove(s)
        if len(unused) == 0:
            switches += 1
            unused = set(engines)
            unused.remove(s)
    return str(switches)

def do_one_test_case(file):
    engine_count = int(file.readline())
    engines = []
    for i in xrange(engine_count):
        engines.append(file.readline())
    search_count = int(file.readline())
    searches = []
    for i in xrange(search_count):
        searches.append(file.readline())

    return switch_count(engines, searches)

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
