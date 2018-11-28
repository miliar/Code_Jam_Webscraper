#!/usr/bin/env python3

import sys

def read_configuration():
    configuration = []
    for i in range(4):
        row = list( map( int, sys.stdin.readline().split() ) )
        configuration.append(row)
    return configuration

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for t in range(1, T+1):
        first_row = int(sys.stdin.readline()) - 1
        first_conf = read_configuration()
        second_row = int(sys.stdin.readline()) - 1      
        second_conf = read_configuration()

        in_both = 0
        guessed_num = -1
        for num in first_conf[first_row]:
            if num in second_conf[second_row]:
                in_both += 1
                guessed_num = num

        if in_both == 1:
            print('Case #{:d}: {:d}'.format(t, guessed_num))
        elif in_both > 1:
            print('Case #{:d}: {:s}'.format(t, 'Bad magician!'))
        elif in_both == 0:
            print('Case #{:d}: {:s}'.format(t, 'Volunteer cheated!'))
