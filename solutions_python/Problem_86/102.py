#!/home/chenfzh/bin/python


def calc(line):
    for i in range(line[0], line[1]+1):
        for j in line[2]:
            if i % j != 0 and j % i != 0:
                break;
        else:
            return '%s' % i
    return 'NO'


def readfile(filename):
    f = open(filename)
    c = f.readlines()
    f.close()
    i = 1
    res = []
    while i < len(c):
        tmp = [int(x) for x in c[i].split()][1:]
        tmp.append([int(x) for x in c[i+1].split()])
        res.append(tmp)
        i += 2
    return res


if __name__ == '__main__':
    import sys
    lines = readfile(sys.argv[1])
    for i in range(0, len(lines)):
        print('Case #%d: %s' % (i+1, calc(lines[i])))
