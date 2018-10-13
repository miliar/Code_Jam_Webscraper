#!/usr/bin/python
#-*- coding: utf8 -*-

''' Template for Google Code Jam '''

import sys

def main():
    ''' main '''
    case_num = int(sys.stdin.readline())
    for i in range(1, case_num+1):
        line = sys.stdin.readline().rstrip()
        args = line.split(' ')
        answer = solve(str(args[0]), int(args[1]))
        print('Case #{0:d}: {1}'.format(i, answer))

def solve(pancakes, num):
    ''' solve problem '''
    pancake_states = list(pancakes)
    for i in range(0, len(pancake_states)):
        pancake_states[i] = True if pancake_states[i] == '+' else False

    count = 0
    for i in range(0, len(pancake_states) - num + 1):
        if not pancake_states[i]:
            count += 1
            for j in range(i, i + num):
                pancake_states[j] = not pancake_states[j]

    if all(pancake_states):
        return count
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    main()
