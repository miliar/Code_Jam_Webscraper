from optparse import OptionParser


def solve(input):
    nb = 0
    res = 0
    for c in input:
        d = int(c)
        nb += d
        if d == 0 and nb == 0:
            res += 1
        elif d == 0:
            nb -= 1
        else:
            nb -= 1
    return res

def problem_A(filename):
    with open(filename, 'rU') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        n, input = lines[i+1].split(" ")
        print "Case #%d: %d" % (i+1, solve(input))



if __name__ == "__main__":
    problem_A("A-large.in")