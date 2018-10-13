#!/bin/env python3

import sys
import os


def doChallenge(_input_filename):
    try:
        with open(_input_filename, 'r') as f:
            lines = f.read().split('\n')
    except FileNotFoundError:
        print("Input file '" + _input_filename + "' not found !")
        sys.exit()
    except PermissionError:
        print("Input file '" + _input_filename + "' could not be read !")
        sys.exit()
    except Exception:
        print("Unknown shit has happened")
        sys.exit()

    del lines[0] # First line is useless
    for i in range(len(list(filter(None, lines)))):
        length, people = lines[i].split()

        #quick fix
        if length == people:
            print('Case #' + str(i+1) + ': 0 0')
            continue

        length = [int(length)]

        for j in range(int(people)):
            key = length.index(max(length))
            value = length[key]

            del length[key]

            if value%2:
                _ = [value//2, value//2]
            else:
                _ = [value//2-1, value//2]

            length = length[:key] + _ + length[key:]
        
            #print(length)

        print('Case #' + str(i+1) + ': ' + str(max(_)) + ' ' + str(min(_)))




if __name__ == '__main__':
    try:
        sys.argv[1]
    except IndexError:
        print("Usage : " + sys.argv[0] + " filename")
    else:
        doChallenge(sys.argv[1])
