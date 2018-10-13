from math import sqrt
def solve_case(r,t):
    a = 2*r-1
    result = int((sqrt(a**2+8*t)-a)//4)
    return result

def solve_cases(fin, fout):
    nCases = int(fin.readline().strip())
    for i in xrange(nCases):
        # get case
        r,t = map(int, fin.readline().strip().split())
        # solve case
        result = solve_case(r,t)
        fout.write("Case #%d: %s\n"%(i+1, result))
        print "Case #%d: %s\n"%(i+1, result)

from sys import argv
solve_cases(open(argv[1]), open(argv[1].replace("in", "out"), "w"))
