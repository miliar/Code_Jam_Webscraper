import itertools
import sys

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(*args, fillvalue=fillvalue)

def parse_case(lines):
    choice1 = int(lines[0])
    chosen1 = set(lines[choice1].split())
    choice2 = int(lines[5])
    chosen2 = set(lines[5 + choice2].split())
    return (chosen1, chosen2)

def parse_file(in_file):
    return (parse_case(case) for case in grouper(10, in_file.readlines()[1:]))


def run_case(n, case):
    solution = case[0].intersection(case[1])
    print "Case #{0}:".format(n),
    if len(solution) == 0:
        print "Volunteer cheated!"
    elif len(solution) == 1:
        print solution.pop()
    else:
        print "Bad magician!"

if len(sys.argv) < 2:
    exit();
    
with open(sys.argv[1], 'r') as in_file:
    for n, case in enumerate(parse_file(in_file), start=1):
        run_case(n, case)
