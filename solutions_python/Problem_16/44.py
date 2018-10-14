import sys
#from collections import defaultdict

#if (80*(i-1)//signs_len < 80*i//signs_len):
  #sys.stderr.write('.')

def perms(str):
    """
    >>> list(perms("123"))
    """
    if len(str) > 1:
        for perm in perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]
    else:
        yield str

def changes(s):
    i = iter(s)
    last = i.next()
    count = 1
    for character in i:
        if character != last:
            last = character
            count += 1
    return count

def min_size(s, k):
    best = len(s)
    for p in perms(range(k)):
        c = changes([s[i*k + idx] for i in xrange(len(s)/k) for idx in p])
        if c < best:
            best = c
    return best

def do_one_test_case(file):
    k = int(file.readline())
    s = file.readline().strip()
    sys.stderr.write('%d, %s\n' % (k, s))
    #print signs

    return str(min_size(s, k))

def main(argv):
    f = open(argv[1], 'r')
    cases = int(f.readline())
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
