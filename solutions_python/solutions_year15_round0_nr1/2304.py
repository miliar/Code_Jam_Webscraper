from __future__ import print_function


def program(n, levels):
    c = 0
    s = levels[0]
    for i in range(1, n + 1):
        # print("%d %d" % (i, s))
        if s < i:
            c += i - s
            s += i - s
        s += levels[i]
    return c

def main():
    cur = 'A-large'

    inputfile = cur + '.in'
    outputfile = cur + '.out'

    f = open(inputfile)
    of = open(outputfile, 'w')

    size = int(f.readline().strip())
    count = 1

    while size > 0:
        line = f.readline().strip().split(' ')

        n = int(line[0])
        levels = [ int(i) for i in list(line[1]) ]

        res = program(n, levels)
        print("Case #%d: %d" % (count, res))
        print("Case #%d: %d" % (count, res), file=of)

        count += 1
        size -= 1

    f.close()
    of.close()

if __name__ == '__main__':
    main()
