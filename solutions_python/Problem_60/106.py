#!/usr/bin/python

from sys import stdin, stdout

total_cases= int( stdin.readline() )
input = stdin.readlines()
output = []

line_number, case_number = 0, 1
while (case_number <= total_cases):
    N, K, B, T = ( int(n) for n in input[line_number].split(' ') )
    locations = [ int(n) for n in input[line_number+1].split(' ') ]
    speeds = [ int(n) for n in input[line_number+2].split(' ') ]
    line_number += 3

    result = 0
    indexes = range(N)
    indexes.reverse()
    for i in indexes:
        if locations[i] + speeds[i] * T >= B:
            K -= 1
            if K <= 0:
                break;
        else:
            result += K

    if K > 0:
        result = "IMPOSSIBLE"

    output.append("Case #%d: %s\n" % (case_number, result))
    case_number += 1

stdout.writelines(output)
