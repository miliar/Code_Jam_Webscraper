__author__ = 'cwagner'

import sys

def resolve_case(line):
    l = (int(line.split()[0]), [int(i) for i in list(line.split()[1])])
    guests = 0
    summ = 0
    for pos, val in enumerate(l[1]):
        if (guests + summ) < pos:
            guests += pos - (guests + summ)
        summ += val
    return guests

def main():
    file = sys.argv[1]
    with open(file, 'r') as f:
        tests = f.readline()
        i = 1
        for line in f:
            # needed_guests = resolve_case(line)
            l = (int(line.split()[0]), [int(j) for j in list(line.split()[1])])
            guests = 0
            summ = 0
            for pos, val in enumerate(l[1]):
                if (guests + summ) < pos:
                    guests += pos - (guests + summ)
                summ += val
            print "Case #{}: {}".format(i, guests)
            i += 1
    return


if __name__ == '__main__':
    main()
