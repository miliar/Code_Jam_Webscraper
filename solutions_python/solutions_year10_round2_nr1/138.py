#!/usr/bin/python

from sys import stdin, stdout


def split_path(path):
    result = []
    while (path != '/' and path != ''):
        result.append(path)
        slash = path.rfind('/')
        path = path[0:slash]
    return result


total_cases = int( stdin.readline() )
input = stdin.readlines()
output = []

line_number, case_number = 0, 1
while (case_number <= total_cases):
    n, m = input[line_number].split(' ')
    n, m = int(n), int(m)
    line_number += 1

    old_dirs = set()
    for i in range( int(n) ):
        for path in split_path(input[line_number+i].strip()):
            old_dirs.add(path)
    line_number += n

    new_dirs = set()
    for i in range( int(m) ):
        for path in split_path(input[line_number+i].strip()):
            new_dirs.add(path)
    line_number += m

    result = 0
    for dir in new_dirs:
        if dir not in old_dirs:
            result += 1
    output.append("Case #%d: %d\n" % (case_number, result))
    case_number += 1

stdout.writelines(output)
