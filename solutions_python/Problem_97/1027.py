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

def control(content):
    result = []
    count = 1
    for line in content:
        A, B = line.rstrip('\n').split()
        A, B = int(A), int(B)
        pair = []
        for i in range(A, B+1):
            if i <= 10: continue
            n = str(i)
            for j in range(1, len(n)):
                if n[j] == '0': continue
                m = int(n[j:] + n[:j])
                if m > i and m <= B:
                    pair.append((i, m))
        result.append('Case #' + str(count) + ': ' + str(len(set(pair))) + '\n')
        count += 1
    return result

        

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Please set input file as a parameter.')
        sys.exit(1)

    content = read_file(sys.argv[1])
    result = control(content)
    write_file(result)
