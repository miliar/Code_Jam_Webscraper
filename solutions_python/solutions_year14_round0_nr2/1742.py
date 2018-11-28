#codeing=utf8

import sys


def main(infile, outfile):
    index = 0
    for line in open(infile):
        if index == 0:
            index += 1
            continue
        res = get_result(line.strip(), index)
        open(outfile, 'a').write('%s\n' % res)
        index += 1


def get_result(line, index):
    data = line.split()
    C = float(data[0])
    F = float(data[1])
    X = float(data[2])
    time = get_shortest_time(C, F, X)
    return 'Case #%d: %f' % (index, time)


def get_shortest_time(C, F, X):
    shorttest_time = X/2
    for i in range(100000):
        begin = i + 1
        farm_time = get_farm_time(begin, C, F, X)
        if farm_time > shorttest_time:
            break
        else:
            shorttest_time = farm_time
    return shorttest_time


def get_farm_time(begin, C, F, X):
    farm_time = C/2
    for i in range(begin):
        j = i + 1
        if j == begin:
            farm_time += X/(2+j*F)
        else:
            farm_time += C/(2+j*F)
    return farm_time


main(sys.argv[1], sys.argv[2])