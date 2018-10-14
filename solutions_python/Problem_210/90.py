#!/usr/bin/python

import sys, datetime

def solve(ac, aj, c, j):
    if ac == aj == 0:
        return 2
    c.sort()
    j.sort()
    cc = []
    jj = []
    cj = 0
    last_c = ac and (not aj or c[-1][0] > j[-1][0])
    t = (c[-1][1] if last_c else j[-1][1]) - 24*60
    n = m = 0
    cl = 0
    jl = 0
    while n < ac or m < aj:
        if m == aj or (n < ac and c[n] < j[m]):
            if last_c:
                cc.append(c[n][0] - t)
            else:
                cj += 1
                last_c = True
            t = c[n][1]
            cl += c[n][1] - c[n][0]
            n += 1
        else:
            if not last_c:
                jj.append(j[m][0] - t)
            else:
                cj += 1
                last_c = False
            t = j[m][1]
            jl += j[m][1] - j[m][0]
            m += 1
    cc.sort(reverse=True)
    jj.sort(reverse=True)
    while cc:
        if cl + cc[-1] <= 12*60:
            cl += cc.pop()
        else:
            break
    while jj:
        if jl + jj[-1] <= 12*60:
            jl += jj.pop()
        else:
            break
    return 2*len(cc) + 2*len(jj) + cj

def parse(input_file):
    ac, aj = map(int, input_file.readline().strip().split())
    c = []
    for _ in xrange(ac):
        c.append(map(int, input_file.readline().strip().split()))
    j = []
    for _ in xrange(aj):
        j.append(map(int, input_file.readline().strip().split()))
    return (ac, aj, c, j)

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
