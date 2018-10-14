import sys
import math
inputfilename = sys.argv[1]


def get_start(s):
    return int(s[:(len(s) + 1)/2])

def gen_palindrom(start, end):
    s = str(start)
    even = len(s) % 2 == 0
    num = get_start(s)
    size = len(str(num))
    #for n in xrange(num,end):
    sn = str(num)
    while True:
        sizecur = len(sn)
        if sizecur > size:
            if not even:
                    sn = sn[:-1]
            even = not even
            size = sizecur
        palindrom = int('%s%s' % (sn,sn[::-1])) if even else int('%s%s' % (sn, sn[::-1][1:]))
        if palindrom > end:
            return
        yield palindrom
        sn = str(int(sn) + 1)
        

def ispalindrom(num):
    snum = str(num)
    return snum[::-1] == snum


def fair_palidroms(n, m):
    total = 0
    nroot = int(math.ceil(math.sqrt(n)))
    mroot = int(math.sqrt(m))
    found = False
    for x in xrange(nroot, mroot+1):        
        if ispalindrom(x):
            found = True
            break
    if not found:
        return
    first_palindrom = x
    for pal in gen_palindrom(first_palindrom, mroot):
        sq = pal**2
        if ispalindrom(sq):
            yield sq

# lst = list(fair_palidroms(10, 10**30))
    
def solve_problem():
    with open(inputfilename) as fp:
        N = int(fp.readline())
        for pr in range(N):
            n, m = map(int, fp.readline().strip().split())
            print "Case #%s: %s" %(pr+1, len(list(fair_palidroms(n, m))))

solve_problem()