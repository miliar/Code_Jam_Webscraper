import sys


def f(line):
    vals = line.strip().split(' ')[1]
    shys = [int(c) for c in vals]
    allppl = []

    for i, s in enumerate(shys):
        allppl += [i] * s

    maxdiff = 0

    for i, p in enumerate(allppl):
        if p - i > maxdiff:
            maxdiff = p - i

    return str(maxdiff)

if __name__ == '__main__':
    infile = sys.argv[1]
    out = open('out.txt', 'w')
    inf = open(infile, 'r')
    line = inf.readline()
    i = 1

    while line:
        line = inf.readline()
        if line == '':
            break
        combined = 'Case #{}: '.format(i)
        combined += f(line)
        out.write(combined + '\n')
        i += 1

    inf.close()
    out.close()
