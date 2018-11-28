

INFILE = "A-large.in"
OUTFILE = INFILE.replace('.in', '.out')


def solve_case(line):
    smax, aud = line.split()
    smax = int(smax)
    clappers = 0
    friends = 0

    for si, n in enumerate(map(int, aud)):
        if si > clappers:
            nf = si - clappers
            friends += nf
            clappers += nf
        clappers += n

    return friends

in_file = open(INFILE, 'r')
T = int(in_file.readline())
out_file = open(OUTFILE, 'w')

for n in xrange(T):
    line = in_file.readline()
    out_file.write("Case #%d: %d\n" % (n + 1, solve_case(line)))
