#!/usr/bin/env python3

from sys import stdin

if __name__ == '__main__':
    T = int(stdin.readline().strip())
    for i in range(1, T+1):
        a = int(stdin.readline().strip())
        line = set() 
        for j in range(1, 4+1):
            if a == j:
                line = set(stdin.readline().strip().split(' '))
            else:
                stdin.readline().strip().split(' ')
        a = int(stdin.readline().strip())
        for j in range(1, 4+1):
            if a == j:
                line = line.intersection(set(stdin.readline().strip().split(' ')))
            else:
                stdin.readline().strip().split(' ')
        if len(line) == 1:
            result = line.pop()
        elif len(line) > 1:
            result = 'Bad magician!'
        elif len(line) == 0:
            result = 'Volunteer cheated!'
        print('case #{0}: {1}'.format(i, result))
