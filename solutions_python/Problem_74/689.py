import sys
import getopt

def solve_case(num, line):
    parts = line.split(' ')
    num_moves = int(parts[0])

    o_pos = 1
    b_pos = 1
    o_wait = 0
    b_wait = 0
    secs = 0

    for i in range(1, num_moves*2, 2):
        color = parts[i].lower()
        pos = int(parts[i+1])

        my_pos = 0
        my_wait = 0

        if color == 'o':
            my_pos = o_pos
            my_wait = o_wait
        else:
            my_pos = b_pos
            my_wait = b_wait

        steps = abs(pos - my_pos)

        steps -= my_wait

        if steps < 0:
            steps = 0

        steps += 1  # Always takes 1 step to push the button
        secs += steps

        if color == 'o':
            o_pos = pos
            o_wait = 0
            b_wait += steps
        else:
            b_pos = pos
            b_wait = 0
            o_wait += steps

    return 'Case #%d: %d\n' % (num+1, secs)

def solve(argv):
    file = argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()

    with open('a.out', 'w') as f:
        N = int(lines[0])
        
        for testcase, i in enumerate(range(1, N+1, 1)):
            out = solve_case(testcase, lines[i])
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
