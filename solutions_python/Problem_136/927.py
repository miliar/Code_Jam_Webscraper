import sys

def solve(C, F, X):
    t2c = 0
    rate = 2.0
    best = X / rate

    while (True):
        t2c = t2c + C / rate
        rate += F
        current = X / rate + t2c

        if best < current:
            return best
        else:
            best = current

f = open(sys.argv[1], 'r')

line = f.readline()
line = f.readline()

case = 1
while line:
    C, F, X = [float(x) for x in line.split()]

    print 'Case #%d: %.7f' % (case, solve(C, F, X))

    line = f.readline()
    case += 1