# Have never written such a crazy logic ever...am sure there is something more elegant
# Welcome to code jam
# Usage pretty simple: Q2.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput


code = "welcome to code jam"
count = []

infile = fileinput.input()

params = infile.readline()

N,n = 0,0

N = int(params.strip())

while N > n :
    count = []
    for ch in code:
        count.append(0)

    str = infile.readline().strip()

    for sch in str:
        if sch == 'w':
            count[0] += 1
        else:
            if sch in code:
                pos = 1
                while pos < len(code):
                    if sch == code[pos]:
                        count[pos] += count[pos-1]
                        #count[pos-1] = 0
                    pos += 1

        if sch == 'm':
            count[len(code)-1] %= 10000
    n += 1
    op = "%d" % (count[len(code)-1])
    print "Case #%d: %s" % (n, op.zfill(4))

infile.close()            