import sys
inp = open(sys.argv[1]);
outp = open(sys.argv[2], 'w');

T = int(inp.next())

i = 1

def splitNumber(n):
    retval = []
    while n != 0:
        retval = [n % 10] + retval
        n = n / 10
    return retval
def combineNumber(arr):
    retval = 0
    for d in arr:
        retval = retval * 10
        retval = retval + d
    return retval

for line in inp:
    line = line.split()
    A = int(line[0])
    B = int(line[1])
    count = 0
    for n in xrange(A, B + 1):
        nS = splitNumber(n)
        found = []
        for ds in xrange(1, len(nS)):
            mS = nS[ds:] + nS[:ds]
            m = combineNumber(mS)
            if (m >= A and m <= B and m > n and m not in found):
                found = found + [m]
                count = count + 1
    outp.write("Case #%d: %d\n" % (i, count))
    i = i + 1
