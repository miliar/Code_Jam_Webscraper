import sys
import pdb

def rotations(l):
    yield l
    for x in range(1,len(l)):
        yield l[-x:] + l[:-x]

def gen_pairs(A,B):
    for n in range(A,B):
        for m in range(n+1,B+1):
            sn = str(n)
            sm = str(m)
            if len(sn) == len(sm):
                ssn = sorted(list(sn))
                ssm = sorted(list(sm))
                if ssn == ssm:
                    if sm in set(rotations(sn)):
                        yield (n,m)

def process_line(line):
    A,B = [ int(x) for x in line.split() ]
    return len(list(gen_pairs(A,B)))


if __name__ == "__main__":
    f = open(sys.argv[1])
    cases = int(f.next().strip())
    lines = [ f.next().strip() for _ in range(cases) ]
    for i,line in enumerate(lines):
        print "Case #%d: %s" % (i+1,process_line(line))