
import sys
sys.setrecursionlimit(100000)

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')


def readline():
    return fi.readline()


def writeline(line):
    fo.write(line + "\n")


def simulate(cps, farm, production, target):
    t0 = target/cps
    t1 = farm/cps + target/(cps+production)
    if t1 > t0:
        return t0
    return farm/cps + simulate(cps+production, farm, production, target)


T = int(readline())
for t in range(0, T):
    input_numbers = readline().split()
    c = float(input_numbers[0])
    f = float(input_numbers[1])
    x = float(input_numbers[2])

    output = simulate(2, c, f, x)

    writeline("Case #%s: %s"%(t+1, output))