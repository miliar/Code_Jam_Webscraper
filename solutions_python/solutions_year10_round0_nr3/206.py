def read(f):
    t = int(f.readline())
    for i in xrange(t):
        line = f.readline()
        R, k, N = map(int, line.split())
        line = f.readline()
        gs = map(int, line.split())
        assert len(gs) == N
        yield R, k, gs

def main(f):
    for i, (R, k, group) in enumerate(read(f)):
        queue = group[:]
        gain = 0
        for r in xrange(R):
            space = k
            riders = []
            while len(queue) > 0 and space - queue[0] >= 0:
                n = queue.pop(0)
                space -= n
                gain += n
                riders.append(n)
            queue.extend(riders)
        print "Case #%d: %d" % (i + 1, gain)

_input = """
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
""".strip()

_output = """
Case #1: 21
Case #2: 100
Case #3: 20
""".strip()

def test_main(compare=False):
    import sys
    from difflib import unified_diff
    from StringIO import StringIO

    stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        main(StringIO(_input))
        result = sys.stdout.getvalue().strip()
    finally:
        sys.stdout = stdout

    print result

    if compare:
        for line in unified_diff(result.splitlines(), _output.splitlines(),
                                 'Output', 'Expect', lineterm=''):
            print line

        if result == _output:
            print "OK"
        else:
            print "NG"

if __name__ == '__main__':
    # test_main(True)
    import sys
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        main(f)
        f.close()
    else:
        main(sys.stdin)
