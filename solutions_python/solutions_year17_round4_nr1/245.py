#!/usr/bin/python

import sys, datetime

def solve(n, p, g):
    if p == 2:
        even = odd = 0
        for x in g:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        return even + (odd + 1)/2
    elif p == 3:
        mod = [0]*3
        for x in g:
            mod[x % 3] += 1
        count = mod[0]
        m = min(mod[1], mod[2])
        mod[1] -= m
        mod[2] -= m
        count += m
        count += (mod[1] + 2)/3
        count += (mod[2] + 2)/3
        return count


def parse(input_file):
    n, p = map(int, input_file.readline().strip().split())
    g = map(int, input_file.readline().strip().split())
    return (n, p, g)

def main():
    start = datetime.datetime.now()
    input_file = open(sys.argv[1])
    output_file = open(sys.argv[2], "w") if len(sys.argv) > 2 else None
    print "Writing to %s" % sys.argv[2] if output_file else "No output file"
    test_cases = int(input_file.readline().strip())
    print "Test cases:",test_cases
    print '-----------------'
    for tc in xrange(1, test_cases + 1):
        output = "Case #%d: %s" % (tc, solve(*parse(input_file)))
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
