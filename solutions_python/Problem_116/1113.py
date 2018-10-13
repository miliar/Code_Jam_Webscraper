#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     14-04-2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys;
import fileinput;
import array;

LINES_PER_QUESTION=5


def check(data):
    first = data[0]
    if first == 'T':
        first = data[1]

    if first=='.': return None

    for c in data[:4]:
        if c != first and c != 'T':
            return None

    return "%s won"%first

def solve(data):

    for row in range(4):
        result=check(data[row])
        if result != None: return result

    for col in range(4):
        result=check([data[0][col],data[1][col],data[2][col],data[3][col]])
        if result != None: return result

    result=check([data[0][0],data[1][1],data[2][2],data[3][3]])
    if result != None: return result

    result=check([data[3][0],data[2][1],data[1][2],data[0][3]])
    if result != None: return result

    total="".join(data[:4])
    symbol=[s for s in total if s=='.']

    if len(symbol) == 0:
        return 'Draw'

    return 'Game has not completed'


def main():
    data = [line for line in fileinput.input('A-large.in')]
    qcount = int(data[0])

    data = data[1:]

    for i in range(qcount):
        result = solve(data[i*LINES_PER_QUESTION:])
        print("Case #%d: %s"%(i+1,result))

if __name__ == '__main__':
    main()