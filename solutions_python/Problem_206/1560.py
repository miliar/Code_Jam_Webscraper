import sys

challenge = 'A'
size = 'large'
infile = None
outfile = None

def solve(D, horses):
    slowest = None
    for h in horses:
        hours = (D - h[0]) / h[1]
        if slowest == None or hours > slowest[2]:
            slowest = (h[0], h[1], hours)
    cruise = D / slowest[2]
    return cruise

def main(argc, argv):
    cases = int(infile.readline().strip())
    for case in range(cases):
        line = infile.readline().strip().split()
        D = float(line[0])
        N = int(line[1])
        horses = [tuple(map(float, infile.readline().strip().split())) for i in range(N)]
        outfile.write('Case #%d: %0.6f\n' % (case + 1, solve(D, horses)))
    return 0

if __name__ == '__main__':
    infile = open('%s-%s.in' % (challenge, size))
    outfile = open('%s-%s.out' % (challenge, size), 'w')
    main(len(sys.argv), sys.argv)
    outfile.close()
    infile.close()
    sys.exit(0)
