#!/usr/bin/env python3
# encoding: utf-8

import sys


def read_file(fname):
    fd = open(fname)
    times = fd.readline()
    times = int(times.rstrip('\n'))
    content = fd.readlines()[:times]
    fd.close()
    return content

def write_file(result):
    fd = open('b.txt', 'w')
    fd.writelines(result)
    fd.close()

def process(combination, N, S, p):
    total = 0
    for item in combination:
        if item[0] >= p: # normal >= p
            total += 1
        elif item[1] >= p: # surprising >= p
            if S > 0:
                total += 1
                S -= 1
    return total

def control(content):
    result = []
    i = 1
    for line in content:
        combination = []
        line = line.rstrip('\n').split()
        for item in line[3:]:
            base = int(item) // 3
            if int(item) % 3 == 0:
                if int(item) == 0:
                    combination.append([base, base]) # if it is 0
                else:
                    combination.append([base, base + 1]) # normal, surprising
            elif int(item) % 3 == 1:
                combination.append([base + 1, base + 1])
            elif int(item) % 3 == 2:
                combination.append([base + 1, base + 2])
        total = process(combination, int(line[0]), int(line[1]), int(line[2]))
        result.append('Case #' + str(i) + ': ' + str(total) + '\n')
        i += 1
    return result

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Please set input file as a parameter.')
        sys.exit(1)

    content = read_file(sys.argv[1])
    result = control(content)
    write_file(result)
