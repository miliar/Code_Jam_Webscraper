#!/usr/bin/python

def xor(it):
    r = 0
    for e in it:
        r ^= e
    return r

def parse(data):
    cases = []
    for i in range(0, len(data), 2):
        cases.append([ int(c) for c in data[i+1].split(' ') ])
    return cases 

def run(case):
    # xor the case, if not 0 don't bother
    if xor(case) != 0:
        return 0

    # otherwise, simply sort and drop the smallest element
    t = 0
    m = case[0]
    for i in case:
        t += i
        m = m if m<i else i
    return t-m

def output(n, result):
    if result == 0:
        result = "NO"
    else:
        result = str(result)
    return "Case #%d:  %s" % (n, result)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Pass filename"

    inp = sys.argv[1]
    outp,_ = inp.rsplit('.',1)
    outp += ".out"

    f = open(inp, 'r')
    data = [ l.strip() for l in f.readlines() ]
    data = data[1:]
    f.close()

    cases = parse(data)

    out = open(outp, 'w')
    for i,case in enumerate(cases):
        result = run(case)
        out.write( output(i+1, result) )
        out.write("\n")
    out.close()
