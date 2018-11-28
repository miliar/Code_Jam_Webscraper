
import math

def readinput(filename):
    f = open(filename, 'r')
    cases = int(f.readline().strip())
    for i in range(cases):
        yield tuple(int(x) for x in f.readline().strip().split())

# http://stackoverflow.com/a/199218
def ispali(num):
    n = num
    rev = 0
    while num > 0:
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    return n==rev

def jee(p, start, end):
    return start <= p <= end and ispali(p)

def fsq(start, end):
    start_sq = int(math.floor(math.sqrt(start)))
    end_sq = int(math.ceil(math.sqrt(end)))
    palis = set(tuple(i for i in xrange(start_sq,end_sq+1) if ispali(i)))
    return len(tuple(1 for p in palis if jee(p*p, start, end)))


case = 1
infile = 'C-small-attempt0.in'
outfile = infile+'.out'
of = open(outfile, 'w')
for start,end in readinput(infile):
    s = "Case #%i: %i\n" %(case, fsq(start,end))
    #print s
    of.write(s)
    case += 1



