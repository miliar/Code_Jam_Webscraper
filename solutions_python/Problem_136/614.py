import itertools
import sys

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

def parse_case(line):
    return map(float, line.split())

def parse_file(in_file):
    return (parse_case(case) for case in in_file.readlines()[1:])


def run_case(n, case):
    c, f, x = case
    nf = max(0, int( (f * x - 2 * c) / (f * c) ))
    time = x / (2 + f * nf) + sum( c /(2 + i * f) for i in range(0,nf))
    print "Case #{0}: {1}".format(n, time)

if len(sys.argv) < 2:
    exit();
    
with open(sys.argv[1], 'r') as in_file:
    for n, case in enumerate(parse_file(in_file), start=1):
        run_case(n, case)
