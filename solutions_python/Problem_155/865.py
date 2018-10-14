import sys


def invite(ns):
    result = 0
    tot = 0
    for s, n in enumerate(map(int, ns)):
        to_invite = max(0, s - tot)
        result += to_invite
        tot += to_invite + n

    return result


def test():
    assert invite("1111") == 0
    assert invite("09") == 1
    assert invite("110011") == 2
    assert invite("1") == 0


if __name__ == "__main__":
    test()
    infile = sys.argv[1] + '.in'
    outfile = sys.argv[1] + '.out'

    data = open(infile).readlines()

    with open(outfile, 'w') as out:
        for i, line in enumerate(data[1:], 1):
            ns = line.strip().split()[1]
            out.write("Case #%i: %i\n" % (i, invite(ns)))
