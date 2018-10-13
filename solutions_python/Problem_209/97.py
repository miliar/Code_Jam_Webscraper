#!/usr/bin/python

import sys, datetime
from math import pi

def solve(n, k, rh):
    sc = []
    for r, h in rh:
        sc.append(r*h)
    ind = sorted(xrange(n), key=lambda i:sc[i], reverse=True)
    j = max(xrange(k), key=lambda i:rh[ind[i]][0])
    b = sum(sc[ind[i]] for i in xrange(k))
    R = rh[ind[j]][0]
    m = R**2 + 2*b
    for i in xrange(k, n):
        R2 = rh[ind[i]][0]
        if R2 > R:
            m = max(m, R2**2 + 2*(b + sc[ind[i]] - sc[ind[k - 1]]))
    return pi*m

def parse(input_file):
    n, k = map(int, input_file.readline().strip().split())
    rh = []
    for i in xrange(n):
        rh.append(map(int, input_file.readline().strip().split()))
    return (n, k, rh)

def main():
    start = datetime.datetime.now()
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    print "Writing to %s" % sys.argv[2] if output_file else "No output file"
    test_cases = int(input_file.readline().strip())
    print "Test cases:",test_cases
    print '-----------------'
    for tc in xrange(1, test_cases + 1):
        output = "Case #%d: %.9f" % (tc, solve(*parse(input_file)))
        print output
        if output_file:
            output_file.write(output + "\n")
    print '-----------------'
    print "Written to %s" % sys.argv[2] if output_file else "No output file"
    print 'Elapsed time: %s' % (datetime.datetime.now() - start)
    input_file.close()
    if output_file:
        output_file.close()

if __name__ == "__main__":
    main()
