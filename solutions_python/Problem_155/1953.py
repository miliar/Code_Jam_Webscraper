__author__ = 'elubin'
import fileinput

class Crowd:
    def __init__(self, peeps):
        self.peeps = peeps

    def solve(self):
        num_standing = 0
        num_needed = 0
        for i, x in enumerate(self.peeps):
            if x > 0:
                # there are people that need to stand
                if num_standing < i:
                    n = i - num_standing
                    num_needed += n
                    num_standing += n
                num_standing += x
        return num_needed


if __name__ == '__main__':
    input = fileinput.input()
    lines = []
    for x in input:
        lines.append(x)

    num_tests = int(lines[0])
    for i in range(num_tests):
        t = lines[i + 1]
        peeps = []
        num_peeps, rest = t.split()
        for j in range(int(num_peeps) + 1):
            peeps.append(int(rest[j]))
        print 'Case #%d: %d' % (i + 1, Crowd(peeps).solve())