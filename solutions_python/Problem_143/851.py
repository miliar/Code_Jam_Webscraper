import sys
from copy import deepcopy as copy

# fpIn = open("ex.in", "r")
# fpOut = open("ex.out", "w")
fpIn = open("small.in", "r")
fpOut = open("small.out", "w")
# fpIn = open("large.in", "r")
# fpOut = open("large.out", "w")

def raw_input():
    return fpIn.readline().strip()


class Print(object):
    def __init__(self, f):
        self.f = f

    def write(self, text):
        fpOut.write(text)
        self.f.write(text)

    def flush(self):
        fpOut.flush()
        self.f.flush()

def do_test():
    A,B,K = [int(x) for x in raw_input().split()]
    count = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                count += 1
    return str(count)


def main():
    line = raw_input()
    num_tests = int(line)
    for i in range(num_tests):
        print "Case #" + str(i+1) + ": " + do_test()

if __name__ == '__main__':
    if not isinstance(sys.stdout, Print):
        sys.stdout = Print(sys.stdout)
    main()