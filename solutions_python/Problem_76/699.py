import sys
import getopt
import itertools

def solve_case(num, line):
    candies = map(int, line.split(' '))
    combos = []
    pairs = []

    answer = 0

    for i in range(1, len(candies)):
        combos.extend(list(itertools.combinations(candies, i)))

    for c in combos:
        rest = candies[:]
        for i in c:
            if i in rest:
                rest.remove(i)

        # pairs.append([c, list(set(candies) - set(c))])
        pairs.append([c, rest])

    for p in pairs:
        a = reduce(lambda x, y: x ^ y, p[0])
        b = reduce(lambda x, y: x ^ y, p[1])
        sum_a = sum(p[0])
        sum_b = sum(p[1])
        m = max(sum_a, sum_b)

        if (a == b) and (m > answer):
            answer = m
            
    if answer == 0:
        answer = 'NO'

    return 'Case #%d: %s\n' % (num+1, answer)

def solve(argv):
    file = argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()

    with open('c.out', 'w') as f:
        N = int(lines[0])
        
        for testcase, i in enumerate(range(1, N*2, 2)):
            out = solve_case(testcase, lines[i+1])
            f.write(out)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'h', ['help'])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, 'for help use --help'
        return 2

    solve(argv)

if __name__ == '__main__':
    sys.exit(main())
