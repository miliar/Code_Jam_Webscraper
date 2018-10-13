import sys
#from collections import defaultdict

#if (80*(i-1)//signs_len < 80*i//signs_len):
  #sys.stderr.write('.')

def dbl_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    ret = abs((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))
    return ret

def get_tri_coords(N, M, A):
    if A > M * N:
        return None
    ps = [(x, y) for x in xrange(N+1) for y in xrange(M+1)]
    p1 = (0, 0)
    for p2 in ps:
        for p3 in ps:
            if dbl_area(p1, p2, p3) == A:
                return list(p1) + list(p2) + list(p3)
    return None


def do_one_test_case(file):
    N, M, A = (int(v) for v in file.readline().split())
    sys.stderr.write('%s\n' % str((N, M, A)))
    coords = get_tri_coords(N, M, A)
    if coords:
        return " ".join([str(c) for c in coords])
    else:
        return "IMPOSSIBLE"

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
