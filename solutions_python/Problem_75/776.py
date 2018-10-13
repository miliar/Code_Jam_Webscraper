#!/usr/bin/python

def itoa(i):
    return chr(i+65)

def wtoi(s):
    ints = [ ord(c.upper())-65 for c in s ]
    return [ i for i in ints if i>=0 and i<=25 ]

# global defs

class Case(object):
    def __init__(self):
        self.pairs = {}
        self.opposed = {}

    def get_pair(self, a, b):
       if self.pairs.has_key(a):
           if self.pairs[a][0] == b:
               return self.pairs[a][1]
       return -1

    def get_opposed(self, a):
        return self.opposed.get(a, -1)

    def add_pair(self, s):
        p = wtoi(s)
        self.pairs[p[0]] = (p[1], p[2])
        self.pairs[p[1]] = (p[0], p[2])

    def add_opposed(self, s):
        p = wtoi(s)
        print "Opp: %s" % s, p
        self.opposed[p[0]] = p[1]
        self.opposed[p[1]] = p[0]

def parse(data):
    cases = []
    i = 1
    for row in data:
        print "Case #%d:" % i
        case = Case()
        info = row.split(' ')

        pair_c = int(info[0])
        for pair in info[1:pair_c+1]:
            case.add_pair(pair)
        info = info[pair_c+1:]

        opp_c = int(info[0])
        for opp in info[1:opp_c+1]:
            case.add_opposed(opp)

        case.inp = wtoi(info[-1])
        cases.append(case)
        i+=1
        print '----------------'

    return cases

def run(case):
    inp = case.inp

    prev = -1
    outp = []

    print "Inp: " + ''.join([itoa(i) for i in inp])
    print "Pairs: ", ', '.join([itoa(p) + itoa(case.pairs[p][0]) + itoa(case.pairs[p][1]) for p in case.pairs.keys()])
    print "Opps: ", ", ".join([itoa(k) + itoa(case.opposed[k]) for k in case.opposed.keys()])
    for e in inp:
        # check for pairs
        pair = case.get_pair(prev, e)
        opp = case.get_opposed(e)
        if pair != -1:
            act = "pair"
            outp[-1] = pair
            prev = pair
        elif opp!=-1 and (opp in outp):
            act = "clr!"
            outp = []
            prev = -1
        else:
            act = "else"
            outp.append(e)
            prev = e
        print "%s: %s %s %s -> %s" % (act, itoa(e), itoa(pair), itoa(opp), ''.join([itoa(i) for i in outp]))

    print "--------------------------"
    return outp

def output(n, result):
    result = [ itoa(i) for i in result ]
    return "Case #%d: [%s]" % (n, ', '.join(result))

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
        print "Case #%d:  "%i
        result = run(case)
        out.write( output(i+1, result) )
        out.write("\n")
    out.close()
